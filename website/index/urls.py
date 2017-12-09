from django.conf.urls import url
from django.conf.urls.static import static

from index.views import HomeView

from django.conf import settings

urlpatterns = [
    url(r'^$', HomeView.as_view(),name='index'),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
