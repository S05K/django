from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListAPIView
# Create your views here.
from rest_framework import generics
from rest_framework import mixins
from practice.models import Account
from practice.serializers import AccountSerializer

class AccountView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)
    
    def post(self, request, *args, **kwargs):
        return self.create(request)
    

class AccountDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin, 
                    generics.GenericAPIView):
    
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request)
    
    def put(self, request, *args, **kwargs):
        return self.update(request)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request)
