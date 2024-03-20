# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

class sqlserverconn(models.Models):
    ID = models.IntegerField(max_length = 100)
    lat_coord = models.DecimalField(max_length = 100)
    long_coord = models.DecimalField(max_length = 100)
    soil_moisture = models.DecimalField(max_length = 100)
    soil_temp = models.DecimalField(max_length = 100)
    atm_moisture = models.DecimalField(max_length = 100)
    atm_temp = models.DecimalField(max_length = 100)
    light_intensity = models.DecimalField(max_length = 100)
    nitro_cont = models.DecimalField(max_length = 100)
    phos_cont = models.DecimalField(max_length = 100)
    soil_ph = models.DecimalField(max_length = 100)
    

