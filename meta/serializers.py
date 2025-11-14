from rest_framework import serializers
from .models import District, Slot

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ["id","name"]

class SlotsSerializer(serializers.Serializer):
    value = serializers.CharField()
    label = serializers.CharField()
