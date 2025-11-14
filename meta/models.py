from django.db import models

class District(models.Model):
    name = models.CharField(max_length=80, unique=True)  # фиксированный список
    def __str__(self): return self.name

class Slot(models.TextChoices):
    S09_11 = "09-11", "09:00–11:00"
    S11_13 = "11-13", "11:00–13:00"
    S13_15 = "13-15", "13:00–15:00"
    S15_17 = "15-17", "15:00–17:00"
    S17_19 = "17-19", "17:00–19:00"
    S19_21 = "19-21", "19:00–21:00"
