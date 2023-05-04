from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include('allauth.urls')),
    path("residents/", include("residents.urls")),
    path("", include("landing.urls")),
    path("main/", include("mainApp.urls")),
    path("main/communications/", include("communications.urls")),
    path("main/events/",include("events.urls")),
    path("main/payment/", include("payment.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
