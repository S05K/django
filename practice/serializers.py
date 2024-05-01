from rest_framework import serializers 
from practice.models import Account

class AccountSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, required=True) 
    email = serializers.CharField(max_length=200, required=True) 

    class Meta:
        model = Account
        fields = ['id','name', 'email']