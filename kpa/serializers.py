from rest_framework import serializers
from .models import WheelSpecification
import re
class WheelSerializer(serializers.ModelSerializer):
    class Meta:
        model=WheelSpecification
        fields='__all__'


    def validate_formNumber(self, value):
        pattern = r'^wheel-\d{4}-\d{3}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("formNumber must be in format 'wheel-YYYY-NNN'")
        return value
    
    def validate_submittedBy(self,value):
        pattern=r'^user_id_\d{3}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("submittedBy must be in format 'user-id-NNN'")
        return value

