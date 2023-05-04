from django.shortcuts import render
from django.views import View
from .forms import Event_Entry
from .models import Event
from django.urls import reverse_lazy
from django.views.generic import DeleteView

# Create your views here.

class Event_Form(View):
    def get(self, request, *args, **kwargs):
        event_posts = Event.objects.all().order_by("-created")
        form = Event_Entry()

        context = {
            "event_list":event_posts,
            "form":form,
        }

        return render(request, "add_event.html", context)

    def post(self, request, *args, **kwargs):
        event_posts = Event.objects.all().order_by("-created")
        form = Event_Entry(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post = form.save()

        context = {
            "event_list":event_posts,
            "form":form,
        }

        return render(request, "events_list.html", context)


class Events(View):
    def get(self, request, *args, **kwargs):
        event_posts = Event.objects.all().order_by("-created")
        form = Event_Entry()

        context = {
            "event_list":event_posts,
            "form":form,
        }

        return render(request, "events_list.html", context)

    # def post(self, request, *args, **kwargs):
    #     event_posts = Event.objects.all().order_by("-created")
    #     form = Event_Entry(request.POST)
    #
    #     if form.is_valid():
    #         new_post = form.save(commit=False)
    #         new_post.author = request.user
    #         new_post = form.save()
    #
    #     context = {
    #         "event_list":event_posts,
    #         "form":form,
    #     }
    #
    #     return render(request, "events_list.html", context)
