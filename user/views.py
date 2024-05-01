from django.http import HttpResponse
from django.shortcuts import render
from user.models import Students
from user.serializers import *
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# Create your views here.
import pdb

class StudentView(APIView):

    def get(request, self, user_id=None):
        if user_id is not None:
            obj = Students.objects.get(id=user_id)
            serializers = StudentSerializer(obj)
            return Response({'status':'success', "students":serializers.data}, status=200)
        else:
            result = Students.objects.all()
            serializers = StudentSerializer(result, many=True)
            return Response({'status':'success', "students":serializers.data}, status=200)
    

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, user_id):
        obj = Students.objects.get(id=user_id)
        obj.delete()
        return Response("data is deleted", status=status.HTTP_201_CREATED)
    

    def patch(self, request, user_id):
        # pdb.set_trace()
        try:
            student = Students.objects.get(id=user_id)
        except Students.DoesNotExist:
            return Response("Student not found", status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserView(APIView):

    def get(request, self):
        obj = CustomUser.objects.all()
        serializers = UserSerializer(obj, many=True)
        return Response({'users':'succes', 'data':serializers.data})



    def post(self,request):
        # pdb.set_trace()
        password = make_password(request.data.get('password'))
        request.data['password'] = password
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
                # serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserLoginView(APIView):
    def post(self, request):
        # pdb.set_trace()
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            serializers = UserSerializer(user)
            return Response({'user': serializers.data, 'token':token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
