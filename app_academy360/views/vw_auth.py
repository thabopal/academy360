from pyexpat.errors import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

from app_academy360.views import vw_home, vw_auth

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
                return vw_home.index(request)  # Redirect to a success page
            else:
                return vw_home.show_message(request, "Authentication failed")
        except KeyError:
            return vw_home.show_message(request, "Missing username or password")
    else:
        return vw_home.show_message(request, "Invalid request method")

    

def user_logout(request):
    logout(request)
    return vw_auth.user_login(request)

