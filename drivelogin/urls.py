from django.urls import path
from django.urls.conf import include
from .views import AuthorizeDefaultUser

urlpatterns = [
    path('auth/', AuthorizeDefaultUser.as_view())
]
