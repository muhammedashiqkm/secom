from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='images/')  # Using ImageField for image uploads

    def __str__(self):
        return self.name
