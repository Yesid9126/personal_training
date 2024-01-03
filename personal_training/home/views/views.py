# views.py
from django.db.models import Prefetch
from django.views.generic import TemplateView

from personal_training.home.models.models import Carousel1, Carousel2, Carousel4, Carousel5, Identifier, Section3Point


class HomeView(TemplateView):
    template_name = "users/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add custom data to the context
        context["home"] = Identifier.objects.prefetch_related(
            Prefetch("carousels", queryset=Carousel1.objects.all(), to_attr="head_carousels"),
            Prefetch("section2__carousels", queryset=Carousel2.objects.all(), to_attr="ss_carousels"),
            Prefetch("section3__points", queryset=Section3Point.objects.all(), to_attr="ts_points"),
            Prefetch("section4__carousels", queryset=Carousel4.objects.all(), to_attr="fs_carousels"),
            Prefetch("section5__carousels", queryset=Carousel5.objects.all(), to_attr="fi_carousels"),
        ).first()
        return context
