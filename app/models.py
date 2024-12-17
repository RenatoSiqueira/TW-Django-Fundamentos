from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=115)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
