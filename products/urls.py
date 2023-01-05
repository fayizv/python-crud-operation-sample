from unicodedata import name
from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('register', views.register, name='register'),
    path('login',views.user_login, name='login'),
    path('logout',views.user_logout,name='logout'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('edit_profile/<int:id>', views.edit_profile, name='edit_profile'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('add_user',views.add_user,name='add_user'),
    path('search',views.search,name='search'),
]