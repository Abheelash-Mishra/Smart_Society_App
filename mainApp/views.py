from django.shortcuts import render
from django.views import View

# Create your views here.

class MainPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, "main_page.html")
