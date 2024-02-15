from django.http import JsonResponse

from personal_training.courses.models.models import Course
from personal_training.users.models import Cart, User

# Create your views here.


def update_cart(request):
    courses = request.POST.getlist("courses[]")
    cart = request.user.cart if hasattr(request.user, "cart") else None
    if not cart and isinstance(request.user, User):
        cart = Cart.objects.create(user=request.user)
    elif not isinstance(request.user, User):
        return JsonResponse({"message": "User not found"})
    cart.courses.set(Course.objects.only("pk").filter(slug_name__in=courses))
    return JsonResponse({"message": "It worked fine"})
