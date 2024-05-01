from rest_framework import serializers  
from user.models import Students  
from user.models import CustomUser
import pdb
class StudentSerializer(serializers.ModelSerializer):  
    first_name = serializers.CharField(max_length=200, required=True)  
    last_name = serializers.CharField(max_length=200, required=True)  
    address = serializers.CharField(max_length=200, required=True)  
    roll_number = serializers.IntegerField() 
    mobile = serializers.CharField(max_length=10, required=True) 

    def validate_roll_number(self, value):
        if Students.objects.filter(roll_number=value):
            raise serializers.ValidationError("Roll no must be unique")
        return value

    def validate_mobile(self, value):
        if value is None:
            raise serializers.ValidationError("Mobile cannot be empty")
        return value

    def validate_mobile(self, value):
        # pdb.set_trace()
        if Students.objects.filter(mobile=value).exists():
            raise serializers.ValidationError("This mobile no is already regsitered")
        return value

    class Meta:
        model = Students
        fields = ['id','first_name', 'last_name', 'address', 'roll_number', 'mobile']

class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id','username', 'email', 'password']


