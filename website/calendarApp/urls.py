from django.conf.urls import url
from django.conf.urls.static import static

from django.conf import settings
from calendarApp.views import Cal_View

urlpatterns = [
    url(r'^$', Cal_View.as_view(),name='cal'),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
