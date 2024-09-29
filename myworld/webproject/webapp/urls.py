from django.urls import path
from . import views
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView

def home_redirect(request):
    return redirect('login') 

urlpatterns = [
    path('', home_redirect), 
    path('home/', views.BASE, name='BASE'),
    path('login/', LoginView.as_view(), name='login'),
    path('blank/', views.BLANK, name='BLANK'),
    path('tables/', views.TABLES, name='TABLES'),
    path('api/users/', views.user_list, name='user_list'),
    path('api/add_user/', views.add_user, name='add_user'),
    path('api/update_user/<int:user_id>/', views.update_user, name='update_user'),
    path('api/delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('create_user/', views.create_user, name='create_user'),
]
