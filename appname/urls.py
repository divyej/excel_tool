# appname/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('upload/', views.upload_excel, name='upload_excel'),
    path('accounts/profile/', views.upload_excel, name='upload_excel'),
    path('save-excel-data/', views.save_excel_data, name='save_excel_data'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
]
