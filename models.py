from django.db import models
from django.db.models import *
from django.template.defaultfilters import slugify

"""
class Example(models.Model):
    charfield = models.CharField(max_length=100, null=False, blank=False, primary_key=True)
    intfield = models.IntegerField(null=True, blank=True)
    boolfield = models.NullBooleanField()
    decimalfield = models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)
    textfield = models.TextField(null=True, blank=True)

    class Meta:
        db_table = u'example'

    def __unicode__(self):
        return self.charfield

    def save(self):
        print self.charfield
        super(Example, self).save()
"""