from django.shortcuts import render
from django.conf.urls.static import static
# Create your views here.
def home(request):
	return render(request, "calendarTemplate/index.html")