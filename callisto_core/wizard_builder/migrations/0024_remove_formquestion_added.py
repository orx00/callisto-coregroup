# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 23:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callisto_core.wizard_builder', '0023_formquest_text_tinymce'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formquestion',
            name='added',
        ),
    ]