from django.urls import path
from practice.views import AccountView, AccountDetail

urlpatterns=[
    path("/", AccountView.as_view(), name="account-list"),
    path("/<int:pk>",AccountDetail.as_view(), name="account-detail")
]