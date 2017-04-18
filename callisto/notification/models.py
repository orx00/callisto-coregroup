import six

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail.message import EmailMultiAlternatives
from django.db import models
from django.template import Context, Template
from django.utils.html import strip_tags

from callisto.notification.managers import EmailNotificationQuerySet


@six.python_2_unicode_compatible
class EmailNotification(models.Model):
    """Record of Email constructed in and sent via the project"""
    name = models.CharField(blank=False, max_length=50, primary_key=True)
    subject = models.CharField(blank=False, max_length=77)
    body = models.TextField(blank=False)
    sites = models.ManyToManyField(Site)
    objects = EmailNotificationQuerySet.as_manager()

    def __str__(self):
        return self.name

    def render_body(self, context=None):
        """Format the email as HTML."""
        if context is None:
            context = {}
        current_site = Site.objects.get_current()
        context['domain'] = current_site.domain
        return Template(self.body).render(Context(context))

    def render_body_plain(self, context=None):
        """Format the email as plain text."""
        if context is None:
            context = {}
        html = self.render_body(context)
        cleaned = html.replace('<br />', '\n')
        cleaned = cleaned.replace('<br/>', '\n')
        cleaned = cleaned.replace('<p>', '\n')
        cleaned = cleaned.replace('</p>', '\n')
        return strip_tags(cleaned)

    def send(self, to, from_email, context=None):
        """Send the email as plain text.

        Includes an HTML equivalent version as an attachment.
        """

        if context is None:
            context = {}
        email = EmailMultiAlternatives(self.subject, self.render_body_plain(context), from_email, to)
        email.attach_alternative(self.render_body(context), "text/html")
        email.send()

    def add_site_from_site_id(self):
        if getattr(settings, 'SITE_ID', None):
            self.sites.add(settings.SITE_ID)

    def save(self, *args, **kwargs):
        self.add_site_from_site_id()
        super(EmailNotification, self).save(*args, **kwargs)