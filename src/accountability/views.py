from django.views.generic.base import TemplateView

from . import models

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['murders'] = models.Murder.objects.all()
        return context
