from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email=models.EmailField(unique=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return self.username

class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=300)
    completed=models.BooleanField(default=False)
    Start_Time=models.TimeField(null=True)
    End_Time=models.TimeField(null=True)

    def __str__(self):
        return self.title

