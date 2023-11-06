# appname/models.py
from django.db import models

class ExcelData(models.Model):
    headers = models.JSONField()
    rows = models.JSONField()

    def __str__(self):
        return f"Excel Data {self.pk}"
    
class ExcelFile(models.Model):
    file = models.FileField(upload_to='excel_files/')