from django.db import models

# # Create your models here.
class Voltage(models.Model):
    voltage = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)

# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     slug = models.SlugField(unique=True, max_length=255)
#     content = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     author = models.TextField()