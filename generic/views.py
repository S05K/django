from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from generic.models import *
from generic.serializers import PersonSerializer
from rest_framework import status
import pdb
# Create your views here.

class PersonPost(GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        person = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        person = get_object_or_404(self.get_queryset(), pk=pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        person = get_object_or_404(self.get_queryset(), pk=pk)
        serializers = PersonSerializer(person,data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'data':serializers.data})
        else:
            return Response('Error')


class Listing(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def list(self, request):
        serializers = PersonSerializer(self.get_queryset(), many=True)
        return Response({'data':serializers.data}, status=200)
    

    def post(self, request):
        serializers = PersonSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'data':serializers.data}, status=201)
        else:
            return Response('Not a valid data')