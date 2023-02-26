from django.db import models

# Create your models here.
class CsvPipline(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=30)

class CsvPiplineDetails(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=30)