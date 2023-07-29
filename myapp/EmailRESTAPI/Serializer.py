
from rest_framework import serializers,routers,viewsets
from .models import EmailModel
class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmailModel
        fields="__all__"
        
    