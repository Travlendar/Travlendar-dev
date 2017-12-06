from django.shortcuts import render
from django.conf.urls.static import static

# def home(request):
# 	return render(request, "calendar.html")
from django.views import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index/index.html")
