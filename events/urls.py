from django.urls import path
from .views import Events,Event_Form

urlpatterns = [
    path("", Events.as_view(), name="event_list"),
    path("add/", Event_Form.as_view(), name="add_event")
]