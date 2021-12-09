from django.views import generic
from datetime import datetime


class IndexView(generic.TemplateView):
    template_name = "pdv/index.html"

    def get_context_data(self, **kwargs):
        kwargs['data_atual'] = datetime.now().date()
        return kwargs
