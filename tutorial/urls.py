from django.urls import path
from tutorial.views import CityView

urlpatterns=[
    path("/", CityView.as_view()),
    path("/<int:pk>", CityView.as_view())
]