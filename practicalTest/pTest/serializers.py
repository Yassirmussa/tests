from rest_framework import serializers
from .models import Test

class Testserializer (serializers.ModelSerializer):
     class Meta:
        model = Test
        fields = ['name','msg']