from django.db import models

class Druzinka(models.Model):
    id = models.AutoField(primary_key=True)
    nazov = models.CharField(max_length=100)

    def __str__(self):
        return "Družinka {}".format(self.nazov)

class Pokemon(models.Model):
    nazov = models.CharField(max_length=100)
    druzinka = models.ForeignKey(Druzinka, on_delete=models.CASCADE)

    sila = models.IntegerField(default=0)
    rychlost = models.IntegerField(default=0)
    postreh = models.IntegerField(default=0)
    odolnost = models.IntegerField(default=0)

    energia = models.IntegerField(default=10)
    jedol = models.BooleanField(default=False)

    def __str__(self):
        return "Pokémon {} družinky {}".format(self.nazov, self.druzinka.nazov)
