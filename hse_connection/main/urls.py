from django.urls import path, re_path
from django.conf.urls.static import static
from hse_connection import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(
    	r'^profile/(?P<pk>\d+)$', 
		views.profile, 
		name='profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)