from django.urls import path
from mixins.views import InfoList, InfoDetail
urlpatterns=[
    path("/", InfoList.as_view(), name='informations-list'),
    path("/<int:pk>", InfoDetail.as_view(), name='information-detail'),

]