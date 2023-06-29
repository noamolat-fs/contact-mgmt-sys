from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=12)
    
    def __str__(self):
        return self.name