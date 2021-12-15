from rest_framework import serializers
from .models import Plant, Request

class PlantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


