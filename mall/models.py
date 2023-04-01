from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Stuff(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    detail=models.TextField(max_length=300)
    quantity=models.IntegerField(default=0)
    image=models.ImageField(upload_to="",blank=True,verbose_name='stuff_img')
    pub_date=models.DateTimeField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    stuffs=models.ManyToManyField(Stuff)
    # quantity=models.JSONField()
    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username
