from django.db import models

# Create your models here.

class StatusMap():
    Guvende = 0
    ZorDurumda = 1
    GidaIhtiyaci = 2
    BezIhtiyaci = 3
    CadirIhtiyaci = 4


class PersonInfo(models.Model):
    num = models.IntegerField(primary_key=True)
    stat = models.IntegerField(default=0)
    long = models.FloatField(default=33.33)
    lat = models.FloatField(default=44.44)
    def __str__(self):
        return "person with number: "+str(self.num)
