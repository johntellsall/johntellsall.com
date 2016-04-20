# pylint: disable=E1101

from django.views.generic import TemplateView

from meetup.models import Meeting


class AllstuffView(TemplateView):
    template_name = 'allstuff.html'

    def get_context_data(self):
        return dict(
            meetings=Meeting.objects.all(),
            )

