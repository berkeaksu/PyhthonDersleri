from django.db import models

# Create your models here.

class Slider(models.Model):
    img = models.ImageField(upload_to = 'images')
    header = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50)

#python manage.py makemirations --> db işlemleri
    