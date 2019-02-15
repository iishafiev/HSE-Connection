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
	        return redirect('index')

    # Creates the login form
	else:
		return render(request, 'login/signin.html')