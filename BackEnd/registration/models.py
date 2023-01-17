from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE

class UserType(models.Model):
    name_user_type = models.CharField(verbose_name='Nombre Tipo de Usuario', max_length=45)
    created_at = models.DateField(auto_now_add=True, verbose_name="Fecha de creación", null=True, blank=True)
    updated_at = models.DateField(auto_now=True, verbose_name="Fecha de actualización", null=True, blank=True)
    
    class Meta:
        verbose_name = "Tipo de Usuario"
        verbose_name_plural = "Tipos de Usuarios"

    def __str__(self):
        return self.name_user_type


class IDType(models.Model):
    name_id_type = models.CharField(verbose_name='Nombre Tipo de Identificación', max_length=45)
    created_at = models.DateField(auto_now_add=True, verbose_name="Fecha de creación", null=True, blank=True)
    updated_at = models.DateField(auto_now=True, verbose_name="Fecha de actualización", null=True, blank=True)
    
    class Meta:
        verbose_name = "Tipo de Identificación"
        verbose_name_plural = "Tipos de Identificación"

    def __str__(self):
        return self.name_id_type


class User(AbstractUser):
    id_type_user = models.ForeignKey(IDType, on_delete=CASCADE, verbose_name='Tipo de Identificación', null=True, blank=True)
    id_type_identification = models.ForeignKey(UserType, on_delete=CASCADE, verbose_name='Tipo de Usuario', null=True, blank=True)
    identification_number = models.CharField(verbose_name='Número de Identificación', max_length=45)
    full_name = models.CharField(verbose_name='Nombre Completo', max_length=255)
    telephone = models.CharField(verbose_name='Teléfono', max_length=45)
    email = models.CharField(verbose_name='Correo Electrónico', max_length=255)
    created_at = models.DateField(auto_now_add=True, verbose_name="Fecha de creación", null=True, blank=True)
    updated_at = models.DateField(auto_now=True, verbose_name="Fecha de actualización", null=True, blank=True)
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.username
    
    
