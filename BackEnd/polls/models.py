from django.db import models
from django.db.models import CASCADE
from user.models import User


class Period(models.Model):
    period_name = models.CharField(verbose_name="Nombre Periodo", max_length=45)
    
    class Meta:
        verbose_name = "Periodo"
        verbose_name_plural = "Periodos"

    def __str__(self):
        return str(self.period_name)


class Position(models.Model):
    position_name = models.CharField(verbose_name="Nombre Cargo", max_length=45)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        return str(self.position_name)

class Candidate(models.Model):
    id_user = models.ForeignKey(User, on_delete=CASCADE, verbose_name="Usuario")
    id_position = models.ForeignKey(
        Position, on_delete=CASCADE, verbose_name="Cargo", null=True, blank=True
    )
    id_period = models.ForeignKey(
        Period, on_delete=CASCADE, verbose_name="Periodo", null=True, blank=True
    )
    biography = models.CharField(verbose_name="Biografía", max_length=255)
    total_votes = models.IntegerField(verbose_name="Total Votos")
    
    class Meta:
        verbose_name = "Candidato"
        verbose_name_plural = "Candidatos"

    def __str__(self):
        return str(self.id_user)


class Poll(models.Model):
    id_position = models.ForeignKey(
        Position, on_delete=CASCADE, verbose_name="Cargo", null=True, blank=True
    )
    id_user = models.ForeignKey(User, on_delete=CASCADE, verbose_name="Usuario")
    status = models.PositiveIntegerField(verbose_name="Estado")
    created_at = models.DateField(
        auto_now_add=True, verbose_name="Fecha de creación", null=True, blank=True
    )
    updated_at = models.DateField(
        auto_now=True, verbose_name="Fecha de actualización", null=True, blank=True
    )


    class Meta:
        verbose_name = "Votación"
        verbose_name_plural = "Votaciones"

    def __str__(self):
        return str(self.id_user)