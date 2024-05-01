from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response  
from tutorial.models import City
from tutorial.serializers import CitySerializer
# Create your views here.



class CityView(APIView):
    
    def get(self,request, pk=None):
        if pk is None:
            ans = City.objects.all()
            serializers = CitySerializer(ans, many=True)
            return Response({'data':serializers.data})
        else:
            ans = City.objects.get(pk=pk)
            serializers = CitySerializer(ans, partial=True)
            return Response({'data':serializers.data})
    

    def post(self,request):
        serializers = CitySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'data':serializers.data})
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self, request, pk):
        obj = City.objects.get(pk=pk)
        serializers = CitySerializer(obj,data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'data':serializers.data})
        

    def delete(self,request,pk):
        obj = City.objects.get(pk=pk)
        obj.delete()
        return Response({'data':'deleted'})

