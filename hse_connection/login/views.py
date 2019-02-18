from django.shortcuts import render

def login(request):
   # Checks received user data
   if request.method == 'POST':
      username = request.POST['inputEmail']
      password = request.POST['inputPassword']
      user = authenticate(request, username=username, password=password)
      if user:
         login(request, user)
         return redirect('index')
      else:
         message = "Неправильный логин или пароль"
         return render(request, 'login/signin.html', {'message': message})

   # Creates the login form
   else:
      return render(request, 'login/signin.html')


def register(request):
	if request.method == 'POST':
   		email = request.POST['inputEmail']
   		password = request.POST['inputPassword']
   		password_repeat = request.POST['confirmPassword']
   		name = request.POST['inputName']
   		surname = request.POST['inputSurname']
   		campus = request.POST['inputCampus']
   		faculty = request.POST['inputFaculty']
   		photo = request.POST['inputPhoto']

   		# if User.objects.filter(username=username).exists():
   		# 	message = 'Простите, пользователь с таким именем уже существует'
   		# 	return render(request, 'login/register.html', {'message': message})

   		# elif password != password_repeat:
   		# 	message = 'Неверно повторен пароль'
   		# 	return render(request, 'login/register.html', {'message': message})

   		# else:
   		# 	User.objects.create_user(username=username, password=password)
   		# 	return redirect('login')

	else:
		return render(request, 'login/register.html')