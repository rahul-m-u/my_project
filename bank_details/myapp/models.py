from django.db import models

# Create your models here.


class Bank(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Branch(models.Model):
    ifsc = models.CharField(max_length=70)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    branch = models.CharField(max_length=250)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    district = models.CharField(max_length=120, blank=True, null=True)
    state = models.CharField(max_length=120, blank=True, null=True)
