from django.db import models

# Create your models here.
class laptop(models.Model):
    brand=models.CharField(max_length=50)
    price=models.IntegerField()
    imei=models.CharField(max_length=50,unique=True)
    color=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.brand}"