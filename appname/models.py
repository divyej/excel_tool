# appname/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class ExcelData(models.Model):
    headers = models.JSONField()
    rows = models.JSONField()

    def __str__(self):
        return f"Excel Data {self.pk}"
    
class ExcelFile(models.Model):
    file = models.FileField(upload_to='excel_files/')

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('normal', 'Normal User'),
        ('reviewer', 'Reviewer'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='normal')

    
    # Add related_name arguments to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='customuser_set',  # Change this line
        related_query_name='user',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',  # Change this line
        related_query_name='user',
    )