from django.db import models


class Betriebsstelle(models.Model):
    rl_code = models.CharField(max_length=200)
    langname = models.CharField(max_length=200)
    kurzname = models.CharField(max_length=200)
    typ_kurz = models.CharField(max_length=200)
    typ_lang = models.CharField(max_length=200)
    datum_ab = models.CharField(max_length=200)
    niederlassung = models.CharField(max_length=200)
    regionalbereich = models.CharField(max_length=200)
    letzte_aenderung = models.CharField(max_length=200)
