from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.db.models import CASCADE
from django.conf.global_settings import MEDIA_URL, STATIC_URL
from django.utils import timezone


class AdminAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class AdminAccount(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(
        verbose_name="Correo Electrónico", max_length=255, unique=True, blank=True
    )
    admin_name = models.CharField(verbose_name="Nombre", max_length=255, blank=True)
    is_active = models.BooleanField(verbose_name="Activo", default=True)
    is_staff = models.BooleanField(verbose_name="Es staff", default=False)
    image = models.ImageField(
        verbose_name="Logo", upload_to="profiles/%Y/%m/%d", null=True, blank=True
    )
    date_joined = models.DateTimeField(
        verbose_name="Fecha de Registro",
        default=timezone.now,
    )

    objects = AdminAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "admin_name",
    ]

    def get_image(self):
        if self.image:
            return "{}{}".format(MEDIA_URL, self.image)
        return "{}{}".format(STATIC_URL, "media/img/galeria/profile-default.png")

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Admnistradores"

    def __str__(self):
        return str(self.admin_name)


class UserType(models.Model):
    name_user_type = models.CharField(
        verbose_name="Nombre Tipo de Usuario", max_length=45
    )
    created_at = models.DateField(
        auto_now_add=True, verbose_name="Fecha de creación", null=True, blank=True
    )
    updated_at = models.DateField(
        auto_now=True, verbose_name="Fecha de actualización", null=True, blank=True
    )

    class Meta:
        verbose_name = "Tipo de Usuario"
        verbose_name_plural = "Tipos de Usuarios"

    def __str__(self):
        return str(self.name_user_type)


class IDType(models.Model):
    name_id_type = models.CharField(
        verbose_name="Nombre Tipo de Identificación", max_length=45
    )
    created_at = models.DateField(
        auto_now_add=True, verbose_name="Fecha de creación", null=True, blank=True
    )
    updated_at = models.DateField(
        auto_now=True, verbose_name="Fecha de actualización", null=True, blank=True
    )

    class Meta:
        verbose_name = "Tipo de Identificación"
        verbose_name_plural = "Tipos de Identificación"

    def __str__(self):
        return str(self.name_id_type)


class User(models.Model):
    id_admin = models.ForeignKey(
        AdminAccount, on_delete=CASCADE, verbose_name="Usuario", null=True, blank=True
    )
    id_type_user = models.ForeignKey(
        UserType,
        on_delete=CASCADE,
        verbose_name="Tipo de Usuario",
        null=True,
        blank=True,
    )
    id_type_identification = models.ForeignKey(
        IDType,
        on_delete=CASCADE,
        verbose_name="Tipo de Identificación",
        null=True,
        blank=True,
    )
    first_name = models.CharField(verbose_name="Nombres", max_length=45, blank=True)
    last_name = models.CharField(verbose_name="Apellidos", max_length=45, blank=True)
    identification_number = models.CharField(
        verbose_name="Número de Identificación", max_length=45, blank=True
    )
    telephone = models.CharField(verbose_name="Teléfono", max_length=45, blank=True)
    email = models.CharField(
        verbose_name="Correo Electrónico", max_length=255, unique=True, blank=True
    )
    created_at = models.DateField(
        auto_now_add=True, verbose_name="Fecha de creación", null=True, blank=True
    )
    updated_at = models.DateField(
        auto_now=True, verbose_name="Fecha de actualización", null=True, blank=True
    )

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return str(self.first_name)
