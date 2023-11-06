# projectname/urls.py
from django.contrib import admin
from django.urls import path, include
from appname.views import upload_excel  # Import your app's view function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', upload_excel, name='upload_excel'),  # Use the 'upload_excel' view for the root URL
    path('appname/', include('appname.urls')),  # Include your app's URLs (if necessary)
]
