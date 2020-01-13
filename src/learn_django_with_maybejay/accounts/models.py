from django.db import models

# Create your models here.
class User(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    username = models.CharField(max_length=4)