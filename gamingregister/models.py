from django.db import models


class Register(models.Model):
      name = models.CharField(max_length=60)
      email = models.CharField(max_length=60)
      team = models.CharField(max_length=60)
      age = models.IntegerField()
      number = models.IntegerField()
      gender = models.CharField(max_length=20)
      country = models.CharField(max_length=20)
      password = models.CharField()

def __str__(self):
    return self.name