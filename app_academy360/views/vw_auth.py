from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


def user_login(request):
    return render(request, 'user_login.html')

def user_login_post(request):
    if request.method == 'POST':
        try:
            un = request.POST['username']
            pwd = request.POST['password']
            user = authenticate(username=un, password=pwd)
            if user is not None:
                login(request, user)
                try:
                    return HttpResponseRedirect(reverse('index')) # Assuming 'index' will be the name for vw_home.index
                except: # Fallback if reverse fails (e.g. URL not named yet)
                    return HttpResponseRedirect('/index/')
            else:
                messages.error(request, "Authentication failed. Please check your username and password.")
                return render(request, 'user_login.html')
        except KeyError:
            messages.error(request, "Missing username or password.")
            return render(request, 'user_login.html')
    else:
        messages.error(request, "Invalid request method.")
        return render(request, 'user_login.html')

    

def user_logout(request):
    logout(request)
    # Assuming 'user_login' is the name of the URL for user_login view
    try:
        return HttpResponseRedirect(reverse('user_login'))
    except: # Fallback if reverse fails
        return HttpResponseRedirect('/auth/login/') # Or whatever the direct path is

