from django.db import models


class family(models.Model):
    name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    age = models.IntegerField()
    birth_date = models.DateTimeField()


