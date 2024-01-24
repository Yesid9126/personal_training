from django.db.models import Prefetch

from personal_training.contactus.models.models import Contacts
from personal_training.negocio.models.models import FollowUs, Schedule, Tags, TimeSchedule


def settings_context(request):
    contacts = Contacts.objects.all().values()
    schedule = Schedule.objects.all().prefetch_related(
        Prefetch("times", queryset=TimeSchedule.objects.all().order_by("hour_init"), to_attr="times_set")
    )
    followus = FollowUs.objects.first()
    tags = Tags.objects.all().values()
    # print(tags)
    return {"contacts": contacts, "days": schedule, "socials": followus, "tags": tags}
