from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import *
from rest_framework import mixins
from mixins.models import Information
from mixins.serializers import InformationSerializrer
import pdb
# Create your views here.

class InfoList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializrer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        # pdb.set_trace()
        return self.create(request, *args, **kwargs)

class InfoDetail(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializrer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request)


    def delete(self, request, *args, **kwargs):
        return self.destroy(request)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)