# projectname/urls.py
from django.contrib import admin
from django.urls import path, include
from appname.views import upload_excel, save_excel_data, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/profile/', upload_excel, name='upload_excel'),  # Use the 'upload_excel' view for the root URL
    path('', home, name='home'),  #
    path('appname/', include('appname.urls')),  # Include your app's URLs under 'appname/'
    # Add other paths as necessary
]