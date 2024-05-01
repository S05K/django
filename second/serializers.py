from rest_framework import serializers 
from second.models import Info

class InfoSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=200, required=True)  
    def validate_first_name(self, value):
        if len(value)<5:
            raise serializers.ValidationError("name length sould be greater than or equal to 5")    
        return value
        
    last_name = serializers.CharField(max_length=200, required=True)
    email = serializers.CharField(max_length=200, required= True)
    def validate_email(self,value):
        if Info.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email must be unique")
        return value

    class Meta:
        model = Info
        fields = ['id','first_name', 'last_name', 'email']
        # fields = ('__all__')