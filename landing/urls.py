from django.urls import path
from landing.views import Landing

urlpatterns = [
    path("", Landing.as_view(), name="landing"),
]