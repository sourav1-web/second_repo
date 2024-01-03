from django.db import models

# Create your models here.
class HydJobs(models.Model):
  name=models.CharField(max_length=64)
  title=models.CharField(max_length=64)
  role=models.CharField(max_length=30)
  date=models.DateField()
  phno=models.IntegerField()
  address=models.CharField(max_length=64)

class BangaloreJobs(models.Model):
  name=models.CharField(max_length=64)
  title=models.CharField(max_length=64)
  role=models.CharField(max_length=30)
  date=models.DateField()
  phno=models.IntegerField()
  address=models.CharField(max_length=64)  

class PuneJobs(models.Model):
  name=models.CharField(max_length=64)
  title=models.CharField(max_length=64)
  role=models.CharField(max_length=30)
  date=models.DateField()
  phno=models.IntegerField()
  address=models.CharField(max_length=64)


class Contact(models.Model):
  name=models.CharField(max_length=64)
  email=models.EmailField()
  msg=models.TextField(max_length=120)