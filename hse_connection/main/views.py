from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import UserProfile, Publication

def index(request):
	user = request.user
	if user.is_authenticated:
		return redirect('profile', pk = user.pk)

	else:
		return redirect('login')


def profile(request, pk):
	user = get_object_or_404(User, pk = pk)
	profile = get_object_or_404(UserProfile, user = user)
	publications = Publication.objects.filter(author = user)
	args = {
		'user': user,
		'profile': profile,
		'publications': publications
	}
	return render(request, 'main/profile.html', args)


def feed(request):
	publications = Publication.objects.all()
	return render(request, 'main/feed.html', {'publications': publications})