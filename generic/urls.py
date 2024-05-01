from django.urls import path
from generic.views import PersonPost, Listing
urlpatterns=[
    path("/<int:pk>", PersonPost.as_view(), name='person-detail'),
    path("/", Listing.as_view(), name='person-list')
]