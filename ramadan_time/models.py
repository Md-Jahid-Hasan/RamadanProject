from django.db import models


# Create your models here.
class sehri_iftar_time(models.Model):
    date = models.CharField(max_length=20)
    sehri_hour = models.IntegerField(default=3)
    sehri_minute = models.IntegerField()
    iftar_hour = models.IntegerField(default=6)
    iftar_minute = models.IntegerField()

    def __str__(self):
        return self.date

class District(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name