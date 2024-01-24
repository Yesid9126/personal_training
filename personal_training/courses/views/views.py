# views.py
# from django.db.models import Prefetch
from django.views.generic import TemplateView

from personal_training.courses.models.models import Course


class CoursesView(TemplateView):
    template_name = "courses.html"

    def get_context_data(self, **kwargs):
        query_params = self.request.GET.dict()
        context = super().get_context_data(**kwargs)
        # Add custom data to the context
        tags = context["filters"] = query_params.pop("filters", None) or []
        search = context["search"] = query_params.pop("search", None) or ""
        page_number = query_params.pop("page_number", None) or "1"
        order_by = context["order_by"] = query_params.pop("order_by", None) or "-modified"
        if tags:
            tags = tags.split(",")
            query_params["tags__in"] = context["filters"] = [int(tag.strip()) for tag in tags]
        if search:
            query_params["name__icontains"] = context["search"] = search
        if page_number:
            page_number = context["page_number"] = int(page_number)
        # Add custom data to the context
        course_pks = list(Course.objects.filter(**query_params).values_list("pk", flat=True).order_by("pk").distinct("pk"))
        count = Course.objects.filter(pk__in=course_pks).count()
        page_size = 1

        if page_number * page_size > count:
            page_number = count // page_size + 1

        off_set = (page_number - 1) * page_size
        context["pages"] = [
            {"number": i, "url": f"?page_number={i}" if not query_params else f"&page_number={i}"}
            for i in range(1, count // page_size + 2)
            if i in [page_number - 1, page_number, page_number + 1]
        ]
        context["page_next"] = {
            "flat": context["pages"][-1]["number"] < count // page_size + 1,
            "url": f"""?page_number={context["pages"][-1]["number"]+1}"""
            if not query_params
            else f"""&page_number={context["pages"][-1]["number"]+1}""",
        }
        context["page_previous"] = {
            "flat": page_number > 2,
            "url": f"""?page_number={context["pages"][0]["number"]-1}"""
            if not query_params
            else f"""&page_number={context["pages"][0]["number"]-1}""",
        }

        context["courses"] = list(Course.objects.filter(pk__in=course_pks).order_by(order_by)[off_set : off_set + page_size])
        return context


# class DetailCourseView(TemplateView):
#     template_name = "users/detail-course.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Add custom data to the context
#         context["course"] = Course.objects.prefetch_related(
#             Prefetch("classes", queryset=Class.objects.all(), to_attr="set_classes")
#         ).get(slug_name=kwargs["slug_name"])
#         return context
