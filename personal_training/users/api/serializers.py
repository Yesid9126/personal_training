from rest_framework import serializers

from personal_training.courses.models.models import Course
from personal_training.users.models import Cart, Coupon, User


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password", "groups", "user_permissions"]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    courses = CourseSerializer(many=True, read_only=True)
    coupon = CouponSerializer(read_only=True)
    total = serializers.SerializerMethodField()
    total_with_coupon = serializers.SerializerMethodField()

    def get_total(self, obj):
        return float(obj.total)

    def get_total_with_coupon(self, obj):
        return float(obj.total_with_coupon)

    class Meta:
        model = Cart
        fields = "__all__"
