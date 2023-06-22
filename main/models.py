from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=300)
    description=models.TextField()
    completed=models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def trim(self):
        return self.title[:40]   if self.title > self.title[:40] else self.title

