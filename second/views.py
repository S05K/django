from django.shortcuts import render
from rest_framework import *
from rest_framework.response import Response  
from rest_framework.decorators import api_view
from second.serializers import InfoSerializer
from second.models import Info
from rest_framework import status
import pdb
# Create your views here.

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def hello(request, user_id=None):
    if request.method == 'GET':
        if user_id is None:
            obj = Info.objects.all()
            serializers = InfoSerializer(obj, many =True)
            return Response(serializers.data,status=200)
        else:
            obj = Info.objects.get(id=user_id)
            serializer = InfoSerializer(obj)
            return Response(serializer.data, status=200)
        
    if request.method == 'POST':
        serializer = InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'info':serializer.data}, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        obj = Info.objects.get(id=user_id)
        obj.delete()
        return Response("data is deleted", status=status.HTTP_201_CREATED)
    
    if request.method == 'PUT':
        obj = Info.objects.get(id=user_id)
        serializer = InfoSerializer(obj, data=request.data, partial=True)     
        if serializer.is_valid():
            serializer.save()
            return Response({'info':serializer.data}, status=200)
        else:
            return Response({'error':'Please put valid attribute'})