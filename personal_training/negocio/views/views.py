# views.py
# from django.db.models import Prefetch
from django.views.generic import TemplateView

from personal_training.contactus.models.models import ContactUs, Location


class ContactUsView(TemplateView):
    template_name = "contact-us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add custom data to the context
        context["contactus"] = ContactUs.objects.first()
        context["locations"] = Location.objects.all()
        return context
