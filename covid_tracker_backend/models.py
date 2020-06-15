from django.db import models


class COVIDData(models.Model):
    country = models.CharField(max_length = 100, blank = False, null = False, default = '')
    total_cases = models.IntegerField(blank = False, null = False, default = '')
    new_cases = models.IntegerField(blank = True, null = True, default = '')
    total_deaths = models.IntegerField(blank = False, null = False, default = '')
    new_deaths = models.IntegerField(blank = True, null = True, default = '')
    total_recovered = models.IntegerField(blank = False, null = False, default = '')
    active_cases = models.IntegerField(blank = False, null = False, default = '')
    day = models.DateField(blank = False, null = False, default = '')
