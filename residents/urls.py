from django.urls import path
from .views import Residents

urlpatterns = [
    path("", Residents.as_view(), name="residents"),
]