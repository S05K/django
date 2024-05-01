from rest_framework import serializers 
from mixins.models import Information

class InformationSerializrer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, required=True) 
    address = serializers.CharField(max_length=200, required=True) 
    email = serializers.CharField(max_length=200, required=True) 

    class Meta:
        model = Information
        fields = ['id','name', 'address', 'email']
