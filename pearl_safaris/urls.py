from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.homepage,name = 'home'),
    path('signup/',views.signUp_page,name='signup'),
    path('users/',views.users_list,name='users')
]
