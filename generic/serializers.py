from rest_framework import serializers 
from generic.models import Person

class PersonSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=200, required=True) 
    last_name = serializers.CharField(max_length=200, required=True)
    email = serializers.CharField(max_length=200, required=True)  

    class Meta:
        model = Person
        fields = ['id','first_name', 'last_name', 'email']
