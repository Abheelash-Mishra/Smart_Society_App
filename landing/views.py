from django.shortcuts import render

# Create your views here.
class Landing(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")