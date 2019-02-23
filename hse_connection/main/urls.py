from django.urls import path, re_path
from django.conf.urls.static import static
from hse_connection import settings
from . import views

urlpatterns = [
    path(
    	'', 
    	views.index, 
    	name='index'),
    path(
    	'profile/<int:pk>', 
		views.profile, 
		name='profile'),
    path(
    	'feed',
    	views.feed,
    	name='feed')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)