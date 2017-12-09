from django.shortcuts import render
from django.conf.urls.static import static
# Create your views here.
from django.views import View

class Cal_View(View):
    def get(self, request, *args, **kwargs):
        return render(request, "calendarTemp\calendar.html")
