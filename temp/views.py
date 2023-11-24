from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from temp.models import Profile


def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        phone_number = request.POST['phone_number']

        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                        last_name=last_name)
        profile = Profile.objects.create(user=user, phone_number=phone_number)
        login(request, user)
        return redirect('home')
    return render(request, 'registration/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        phone_number = request.POST['phone_number']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
    return render(request, 'registration/login.html')


class HomePage(TemplateView):
    template_name = 'base.html'