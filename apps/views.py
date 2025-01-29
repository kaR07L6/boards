from django.views.generic import TemplateView

from logging import getLogger

logger = getLogger(__name__)


class HomeView(TemplateView):
    template_name = "index.html"
    extra_context = {"message": "Welcome to the Home Page!"}
