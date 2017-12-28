from django.db import models

class Druzinka(models.Model):
    id = models.AutoField(primary_key=True)
    nazov = models.CharField(max_length=100)

class Pokemon(models.Model):
    nazov = models.CharField(max_length=100)
    druzinka = models.ForeignKey(Druzinka, on_delete=models.CASCADE)

    sila = models.IntegerField(default=0)
    rychlost = models.IntegerField(default=0)
    postreh = models.IntegerField(default=0)
    odolnost = models.IntegerField(default=0)

    energia = models.IntegerField(default=10)
    jedol = models.BooleanField(default=False)
