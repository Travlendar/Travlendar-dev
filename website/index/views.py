from django.shortcuts import render
from django.conf.urls.static import static

def home(request):
	return render(request, "index.html")