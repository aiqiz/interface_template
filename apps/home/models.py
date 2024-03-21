# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class RawData(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    lat_coord = models.DecimalField(db_column='lat_coord', max_digits=10, decimal_places=6, blank=True, null=True)
    long_coord = models.DecimalField(db_column='long_coord', max_digits=10, decimal_places=6, blank=True, null=True)
    soil_moisture = models.DecimalField(db_column='soil_moisture', max_digits=10, decimal_places=4, blank=True, null=True)
    soil_temp = models.DecimalField(db_column='soil_temp', max_digits=10, decimal_places=4, blank=True, null=True)
    atm_moisture = models.DecimalField(db_column='atm_moisture', max_digits=10, decimal_places=4, blank=True, null=True)
    atm_temp = models.DecimalField(db_column='atm_temp', max_digits=10, decimal_places=4, blank=True, null=True)
    light_intensity = models.DecimalField(db_column='light_intensity', max_digits=10, decimal_places=4, blank=True, null=True)
    nitro_cont = models.DecimalField(db_column='nitro_cont', max_digits=10, decimal_places=4, blank=True, null=True)
    phos_cont = models.DecimalField(db_column='phos_cont', max_digits=10, decimal_places=4, blank=True, null=True)
    soil_ph = models.DecimalField(db_column='soil_ph', max_digits=10, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'data'
