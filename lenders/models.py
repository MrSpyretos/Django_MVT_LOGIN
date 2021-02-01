from django.db import models

# Create your models here.

class Lender(models.Model):
    Class=models.CharField(max_length=1)
    Installments=models.IntegerField()
    Amount= models.IntegerField()
    Duration = models.IntegerField()
    def __str__(self):
        return self.name