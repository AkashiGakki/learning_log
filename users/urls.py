from django.urls import path, include
# from django.contrib.auth.views import auth_login
from django.contrib.auth.views import LoginView

import users.views

app_name = 'users'
urlpatterns = [
    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', users.views.logout_view, name='logout'),
    path('register', users.views.register, name='register')
]
