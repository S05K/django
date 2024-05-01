from django import views
from django.urls import path
from second.views import *
from second import views


app_name = "second"

urlpatterns=[
    path('/', hello, name="hello"),
    path('/<int:user_id>', hello, name="hello"),
]