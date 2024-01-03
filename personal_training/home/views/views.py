# views.py
from django.db.models import Prefetch
from django.views.generic import TemplateView

from personal_training.home.models.models import (
    CarouselFiS,
    CarouselFoS,
    CarouselSS,
    HeadCarousel,
    HomeSection,
    PointTS,
)


class HomeView(TemplateView):
    template_name = "users/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add custom data to the context
        context["home"] = HomeSection.objects.prefetch_related(
            Prefetch("headcarousels", queryset=HeadCarousel.objects.all(), to_attr="head_carousels"),
            Prefetch("secondsection__carousels", queryset=CarouselSS.objects.all(), to_attr="ss_carousels"),
            Prefetch("thirdsection__points", queryset=PointTS.objects.all(), to_attr="ts_points"),
            Prefetch("fourthsection__carousels", queryset=CarouselFoS.objects.all(), to_attr="fs_carousels"),
            Prefetch("fifthsection__carousels", queryset=CarouselFiS.objects.all(), to_attr="fi_carousels"),
        ).first()
        return context
