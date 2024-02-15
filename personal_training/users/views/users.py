# Django
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

# Forms
from personal_training.users.forms import SignUpForm

# Models
from personal_training.users.models.checkouts import Cart


class SignUpView(FormView):
    template_name = "users/register.html"
    form_class = SignUpForm

    success_url = reverse_lazy("home:index")

    def form_valid(self, form):
        user = form.save()
        # Force login
        login(self.request, user)
        return super().form_valid(form)


class CartView(TemplateView):
    template_name = "cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add custom data to the context
        if not hasattr(self.request.user, "cart"):
            context["cart"] = Cart.objects.create(user=self.request.user)[0]
            context["cart"]["courses"] = []
        else:
            context["cart"] = {
                "courses": list(self.request.user.cart.courses.all()),
            }

        return context
