from django.db import models
from django.db.models import CASCADE

class Period(models.Model):
    name_period = models.CharField(verbose_name='Nombre Periodo', max_length=45)

class Position(models.Model):
    name_position = models.CharField(verbose_name='Nombre Cargo', max_length=45)
    
class Candidate(models.Model):
    id_position = models.ForeignKey(Position, on_delete=CASCADE, verbose_name='Votaciones', null=True, blank=True)
    

class polls(models,Model):
    id_position = models.ForeignKey(Position, on_delete=CASCADE, verbose_name='Votaciones', null=True, blank=True)