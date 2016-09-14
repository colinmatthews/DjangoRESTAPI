from django.db import models

# Create your models here.


class Clinic(models.Model):

    name = models.TextField()
    streetNumber = models.IntegerField()
    unitNumber = models.CharField(max_length=10,blank=True,null=True )
    streetName = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=3)
    country = models.CharField(max_length=30)
    postalCode = models.CharField(max_length=6)

    phone = models.CharField(max_length=10)
    availableTimes = models.CharField(max_length=200)

    def __str__(self):
        return self.name



