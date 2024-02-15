from django.db.models import Prefetch

from personal_training.contactus.models.models import Contacts
from personal_training.negocio.models.models import FollowUs, Schedule, Tags, TimeSchedule
from personal_training.users.models.checkouts import Cart
from personal_training.users.models.users import User


def settings_context(request):
    contacts = Contacts.objects.all().values()
    schedule = Schedule.objects.all().prefetch_related(
        Prefetch("times", queryset=TimeSchedule.objects.all().order_by("hour_init"), to_attr="times_set")
    )
    followus = FollowUs.objects.first()
    tags = Tags.objects.all().values()
    # print(tags)
    if not isinstance(request.user, User):
        cart = None
    elif not hasattr(request.user, "cart"):
        cart = Cart.objects.create(user=request.user)
    else:
        cart = request.user.cart
    cart_courses = list(cart.courses.all().values_list("slug_name", flat=True)) if cart else []
    return {"contacts": contacts, "days": schedule, "socials": followus, "tags": tags, "cart_courses": cart_courses}
