from rest_framework import serializers
from tutorial.models import City

class CitySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, required=True)
    pincode = serializers.IntegerField(required=True)
    def validate_pincode(self, value):
        if City.objects.filter(pincode=value).exists():
            raise serializers.ValidationError("Pincode should be unique")
        return value
        


    class Meta:
        model = City
        fields = ['id','name','pincode']