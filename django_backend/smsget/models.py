from django.db import models

# Create your models here.

class StatusMap():
    Guvende = 1
    ZorDurumda = 2
    GidaIhtiyaci = 4
    BezIhtiyaci = 8
    CadirIhtiyaci = 16
    EnkazAltindayim = 32
    KomsumdanSesGeliyor = 64


class PersonInfo(models.Model):
    num = models.IntegerField(primary_key=True)
    stat = models.IntegerField(default=0)
    long = models.FloatField(default=33.33)
    lat = models.FloatField(default=44.44)
    txt = models.CharField(max_length=255,default="")
    def __str__(self):
        return "person with number: "+str(self.num)
