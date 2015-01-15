from django.db import models

# Create your models here.

class Population(models.Model):
    name = models.CharField(max_length=20,blank=False,null=False,unique=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Sample(models.Model):
    population = models.ForeignKey(Population, null=True, blank=True)
    name = models.CharField(max_length=20,blank=False,null=False,unique=True)
    sample_date = models.DateField(null=True,blank=False)
    lat = models.FloatField(blank=True,null=True)
    lon = models.FloatField(blank=True,null=True)
    dbh = models.FloatField(blank=True,null=True)
    angle_low = models.FloatField(blank=True,null=True)
    angle_high = models.FloatField(blank=True,null=True)
    angle_distance = models.FloatField(blank=True,null=True)
    height = models.FloatField(blank=True,null=True)
    bark1 = models.FloatField(blank=True,null=True)
    bark2 = models.FloatField(blank=True,null=True)
    bark3 = models.FloatField(blank=True,null=True)
    bark4 = models.FloatField(blank=True,null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

