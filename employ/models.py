from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField

# Create your models here.
class employid(models.Model):
    employ_id=models.IntegerField()
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=50)
    dob=models.DateField()
    sex=models.CharField(max_length=15)
    position=models.CharField(max_length=30)
    date_of_join=models.DateField()
    created=models.DateTimeField(auto_now=True)

