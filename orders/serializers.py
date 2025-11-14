from rest_framework import serializers
from .models import Order, OrderStatus
from meta.serializers import DistrictSerializer
from meta.models import Slot

class OrderListSerializer(serializers.ModelSerializer):
    district = DistrictSerializer()
    client_name = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ["id","amount","district","address","date","slot","notes","photo_url","client_name"]
    def get_client_name(self, obj): return obj.client.first_name or obj.client.email.split("@")[0]

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["district","address","entrance","floor","intercom","date","slot","amount","notes","photo_url"]
    def validate(self, attrs):
        if attrs["amount"] < 500: raise serializers.ValidationError("Минимальное вознаграждение 500 ₸")
        if attrs["slot"] not in [c.value for c in Slot]: raise serializers.ValidationError("Неверный слот")
        return attrs
    def create(self, data):
        user = self.context["request"].user
        return Order.objects.create(client=user, **data)
