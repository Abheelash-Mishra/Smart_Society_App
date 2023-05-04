from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include('allauth.urls')),
    path("residents/", include("residents.urls")),
    path("", include("landing.urls")),
    path("main/", include("mainApp.urls")),
    path("main/communications/", include("communications.urls")),
    path("main/events/",include("events.urls")),
]
