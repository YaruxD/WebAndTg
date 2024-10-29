from django.db import models

class TelegramUsers(models.Model):
    Username = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Username

class TelegramSales(models.Model):
    Username = models.CharField(max_length=100)
    product = models.CharField(max_length=50)
    amount = models.IntegerField()
    state = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.Username} {self.product} {self.state}'

# Create your models here.
