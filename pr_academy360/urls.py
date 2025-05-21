from django.contrib import admin
from django.urls import path
from app_academy360.views import vw_home
from app_academy360.views import vw_auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', vw_home.index, name='home'),
    path('index/', vw_home.index, name='index'),

    # Authentication
    path('', vw_auth.user_login, name='user_login'),
    path('user_login/', vw_auth.user_login, name='user_login_alt'),
    path('user_login_post/', vw_auth.user_login_post, name='user_login_post'),
    path('user_logout/', vw_auth.user_logout, name='user_logout'),
]
