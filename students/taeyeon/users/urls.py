from django.urls import path
from .views import UsersView

urlpatterns = [
    path('/user', UsersView.as_view())
]