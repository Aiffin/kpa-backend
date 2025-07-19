from rest_framework import serializers
from .models import WheelSpecification

class WheelSerializer(serializers.ModelSerializer):
    class Meta:
        model=WheelSpecification
        fields='__all__'
