from django.db import models

# Create your models here.
class Info(models.Model):
    place=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=15)
    email=models.EmailField(max_length=400)

    def __str__(self):
        return self.email
    