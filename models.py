from django.db import models
from django.db.models import *
from django.template.defaultfilters import slugify

class Country(models.Model):
    code = models.CharField(max_length=3, null=False, blank=False, primary_key=True)
    alphacode = models.CharField(max_length=3, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    centerlat = models.DecimalField(max_digits=50, decimal_places=10, null=False, blank=False)
    centerlng = models.DecimalField(max_digits=50, decimal_places=10, null=False, blank=False)
    text = models.TextField(null=True, blank=True)

    class Meta:
        db_table = u'refugees_countries'

    def __unicode__(self):
        return self.name

class State(models.Model):
    stateabbr = models.CharField(max_length=2, null=False, blank=False, primary_key=True)
    statename = models.CharField(max_length=100, null=False, blank=False)
    statelat = models.DecimalField(max_digits=50, decimal_places=10, null=False, blank=False)
    statelng = models.DecimalField(max_digits=50, decimal_places=10, null=False, blank=False)
    stateface = models.CharField(max_length=1)
    text = models.TextField(null=True, blank=True)

    class Meta:
        db_table = u'refugees_states'

    def __unicode__(self):
        return self.statename
        
class Refugee(models.Model):
    countrycode = models.ForeignKey(Country)
    city = models.CharField(max_length=100, null=False, blank=False)
    num = models.IntegerField(null=True, blank=True)
    year = models.CharField(max_length=4)
    notes = models.TextField()
    stateabbr = models.ForeignKey(State)
    
    class Meta:
        db_table = u'refugees'

    def __unicode__(self):
        return self.city + ": " + str(self.num)