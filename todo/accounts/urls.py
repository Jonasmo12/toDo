from django.urls import path
from .views import (
    signUpView,
    loginView,
    logoutView,
)

app_name = 'accounts'

urlpatterns = [
    path('register/', signUpView, name='register'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),

]
