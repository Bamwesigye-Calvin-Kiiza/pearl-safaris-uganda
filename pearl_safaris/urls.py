from django.urls import path
from . import views

app_name = 'pearl_safaris'

urlpatterns = [
    path('home/',views.homepage,name = 'home'),
    path('signup/',views.signUp_page,name='signup'),
    path('users/',views.users_list,name='users'),
    path('',views.landingpage,name='landing page'),
    path('createuser/',views.creat_user_account,name='createuser')
]
