import sys

from django.db import models


class AngkaModel(models.Model):
    masukan = models.DecimalField(decimal_places=0, max_digits=sys.maxsize)
