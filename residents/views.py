from django.shortcuts import render
from django.views import View
from communications.models import Profile


# Create your views here.
class Residents(View):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.all().order_by("-flat_no")

        context = {
            "profile":profile,
        }

        return render(request, "resident_list.html", context)
