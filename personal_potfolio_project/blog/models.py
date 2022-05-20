from django.db import models


class Blog(models.Model):
    description = models.CharField(max_length=50)
    text = models.TextField(max_length=250)
    image = models.ImageField(upload_to='blog/images/')
    date = models.DateField()
