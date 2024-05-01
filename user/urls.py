# from django import views
from user.views import *
from django.urls import path
from user.views import StudentView

urlpatterns =  [
    path('/',StudentView.as_view()),
    path('/<int:user_id>/', StudentView.as_view(),name='student_detail'), 
    path('/post',UserView.as_view()),
    path("/login",UserLoginView.as_view())
]