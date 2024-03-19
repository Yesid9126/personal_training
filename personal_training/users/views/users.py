# Django
# Settings
from django.conf import settings
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

# Serializers
from personal_training.users.api.serializers import CartSerializer

# Forms
from personal_training.users.forms import SignUpForm

# Models
from personal_training.users.models.checkouts import Cart, Checkout, Coupon

# Utils
from personal_training.utils.hashers import get_wompi_signature


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
        coupon_code = self.request.GET.get("coupon_code")
        # Add custom data to the context
        if not hasattr(self.request.user, "cart"):
            cart = Cart.objects.create(user=self.request.user)
            cart.courses.set([])
        else:
            cart = self.request.user.cart
        context["cart"] = {
            "courses": list(cart.courses.all()),
        }
        if cart.coupon and not cart.coupon.is_active:
            cart.coupon = None
            cart.save(update_fields=["coupon"])
        if coupon_code:
            coupon = Coupon.objects.filter(code=coupon_code).first()
            if coupon and coupon.is_active and cart.coupon != coupon:
                cart.coupon = coupon
                cart.save(update_fields=["coupon"])
        context["cart"]["coupon"] = cart.coupon
        context["cart"]["total"] = cart.total
        context["cart"]["total_with_coupon"] = cart.total_with_coupon
        return context


class CartWompiView(TemplateView):
    template_name = "wompi.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add custom data to the context
        if not hasattr(self.request.user, "cart"):
            cart = Cart.objects.create(user=self.request.user)
            cart.courses.set([])
        else:
            cart = self.request.user.cart
        cart_data = CartSerializer(cart).data
        checkout = Checkout.objects.create(cart=cart, historical_cart_json=cart_data, coupon=cart.coupon)
        checkout.courses.set(cart.courses.all())
        context["public_key"] = settings.WOMPI_PUBLIC_KEY
        context["currency"] = "COP"
        context["reference"] = checkout.reference
        context["amount"] = int(cart.total_with_coupon * 100)
        context["signature_integrity"] = get_wompi_signature(
            reference=checkout.reference,
            amount=context["amount"],
            currency="COP",
            integrity_key=settings.WOMPI_INTEGRITY_KEY,
        )
        context["redirect_url"] = self.request.build_absolute_uri(reverse_lazy("users:cart"))
        return context
