from django.shortcuts import render, redirect
from django.contrib.auth import logout as user_logout, authenticate, login as user_login
from django.contrib.auth.models import User

from main.models import UserProfile
from .forms import LoginForm

def login(request):
	# Checks received user data
	if request.method == 'POST':
		email = request.POST['username']
		password = request.POST['password']
		username = User.objects.get(email=email).username
		user = authenticate(request, username=username, password=password)
		if user:
			user_login(request, user)
			return redirect('index')
		else:
			message = "Неправильный логин или пароль"
			return render(request, 'login/signin.html', {'message': message})

	# Creates the login form
	else:
		form = LoginForm
		return render(request, 'login/signin.html', {'form': form})


def register(request):
	if request.method == 'POST':
		name = request.POST['inputName']
		surname = request.POST['inputSurname']
		email = request.POST['inputEmail']
		password = request.POST['inputPassword']
		password_repeat = request.POST['confirmPassword']
		campus = request.POST['inputCampus']
		faculty = request.POST['inputFaculty']
		photo = request.POST['inputPhoto']

		# creates new user
		if User.objects.filter(email = email).exists():
			message = "Пользователь с такой почтой уже зарегистрирован"
			return render(request, 'login/register.html', {'message': message})

		else:
			user = User.objects.create_user(
				username = name + '_' + surname,
				first_name = name,
				last_name = surname,
				email = email,
				password = password
				)

			UserProfile.objects.create(
				user = user,
				avatar = photo,
				campus = campus,
				faculty = faculty
            )

	else:
		return render(request, 'login/register.html')

def logout(request):
	user_logout(request)
	return redirect('login')