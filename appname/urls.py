# appname/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_excel, name='upload_excel'),
    path('save-excel-data/', views.save_excel_data, name='save_excel_data'),
]
