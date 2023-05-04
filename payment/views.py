from django.shortcuts import render
from django.views import View

# Create your views here.
class Payment(View):
    def get(self, request, *args, **kwargs):
        return render(request, "payment_landing.html")

class Portal(View):
    def get(self, request, *args, **kwargs):
        return render(request, "payment.html")

class Success(View):
    def get(self, request, *args, **kwargs):
        return render(request, "success.html")