import logging

from django.http import HttpResponse

from wizard_builder import views as wizard_builder_views

from . import view_helpers, view_partials
from ..reporting import report_delivery

logger = logging.getLogger(__name__)


class EncryptedWizardView(
    view_partials.ReportUpdateView,
    wizard_builder_views.WizardView,
):
    template_name = 'callisto_core/delivery/wizard_form.html'
    done_template_name = 'callisto_core/delivery/review.html'
    steps_helper = view_helpers.ReportStepsHelper

    def dispatch(self, request, *args, **kwargs):
        self._dispatch_processing()
        return super().dispatch(request, *args, **kwargs)


class WizardActionView(
    view_partials.ReportUpdateView,
    EncryptedWizardView,
):
    # NOTE: this is technically a view_partial

    def dispatch(self, request, *args, **kwargs):
        self.kwargs['step'] = view_helpers.ReportStepsHelper.done_name
        return super().dispatch(request, *args, **kwargs)


class WizardPDFView(
    WizardActionView,
):

    def get(self, *args, **kwargs):
        return self._report_pdf_response()

    def _report_pdf_response(self):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="report.pdf"'
        response.write(report_delivery.report_as_pdf(
            report=self.report,
            data=self.storage.cleaned_form_data,
            recipient=None,
        ))
        return response
