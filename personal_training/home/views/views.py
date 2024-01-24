# views.py
from django.db.models import Prefetch
from django.views.generic import TemplateView

from personal_training.courses.models.models import Course
from personal_training.home.models.models import Carousel1, Carousel4, Home, Point3


class HomeView(TemplateView):
    template_name = "users/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add custom data to the context
        context["home"] = Home.objects.prefetch_related(
            Prefetch("carousels1", queryset=Carousel1.objects.all(), to_attr="head_carousels"),
            # Prefetch("carousels2", queryset=Carousel2.objects.all(), to_attr="ss_carousels"),
            Prefetch("points3", queryset=Point3.objects.all(), to_attr="ts_points"),
            Prefetch("carousels4", queryset=Carousel4.objects.all(), to_attr="fs_carousels"),
        ).first()
        context["courses"] = list(Course.objects.all()[:10])
        return context
