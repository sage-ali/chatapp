from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate



from account.forms import RegistrationForm
from account.models import Account

# Create your views here.

def registerPage(request, *args, **kwargs):
	user = request.user
	if user.is_authenticated: 
		# return redirect('home', {'message': f'You are already logged as {user.email}'})
		return redirect('home')
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email').lower()
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			destination = kwargs.get("next")
			if destination:
				return redirect(destination)
			return redirect('home')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form

	return render(request, 'account/register.html', context)

# def registerPage(request):
# 	if request.user.is_authenticated:
# 		return redirect('home')
# 	else:
# 		form = CreateUserForm()
# 		if request.method == 'POST':
# 			form = CreateUserForm(request.POST)
# 			if form.is_valid():
# 				form.save()
# 				user = form.cleaned_data.get('username')
# 				messages.success(request, 'Account was created for ' + user)

# 				return redirect('login')
			

# 		context = {'form':form}
# 		return render(request, 'account/register.html', context)