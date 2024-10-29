from django.db import models

class Catalog(models.Model):
    Type = models.CharField(max_length=40)
    Product = models.CharField(max_length=40)
    Description = models.TextField()
    Photo = models.TextField()
    Price = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.Type} {self.Product}'
# Create your models here.
