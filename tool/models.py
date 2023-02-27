from django.db import models

# Create your models here.
class PiplineDetails(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=30,default=None)
    file_type = models.CharField(max_length=30,default=None)
    file_path = models.CharField(max_length=30,default=None)
    schedule_time = models.CharField(max_length=30,default=None)
    table_name = models.CharField(max_length=30,default=None)
    database_name = models.CharField(max_length=30,default=None)
    

class HiveTableDetails(models.Model):
    file_id = models.ForeignKey(PiplineDetails, on_delete=models.CASCADE, to_field='id')
    column_name = models.CharField(max_length=30)
    file_column_name = models.CharField(max_length=30)
