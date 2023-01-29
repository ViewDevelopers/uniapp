from django.db import models
from django.db.models import CASCADE
from user.models import AdminAccount, User


class CommonZone(models.Model):
    id_admin = models.ForeignKey(
        AdminAccount, on_delete=CASCADE, verbose_name="Administrador"
    )
    zone_name = models.CharField(verbose_name="Nombre Zona", max_length=45)
    quantity = models.IntegerField(verbose_name="Cantidad")
    capacity = models.IntegerField(verbose_name="Capacidad")

    class Meta:
        verbose_name = "Zona Común"
        verbose_name_plural = "Zonas Comunes"

    def __str__(self):
        return str(self.zone_name)


class ZoneRequest(models.Model):
    id_common_zone = models.ForeignKey(
        CommonZone, on_delete=CASCADE, verbose_name="Zona Común"
    )
    id_user = models.ForeignKey(User, on_delete=CASCADE, verbose_name="Usuario")
    date = models.DateField(verbose_name="Fecha de solicitud")
    start_time = models.TimeField(verbose_name="Hora de Inicio")
    end_time = models.TimeField(verbose_name="Hora de Fin")
    request_status = models.PositiveIntegerField(verbose_name="Estado de Solicitud")

    class Meta:
        verbose_name = "Solicitud de Zona"
        verbose_name_plural = "Solicitudes de Zonas"

    def __str__(self):
        return str(self.id_user)


class HousingType(models.Model):
    housing_type_name = models.CharField(
        verbose_name="Nombre Tipo de Vivienda", max_length=45
    )

    class Meta:
        verbose_name = "Tipo de Vivienda"
        verbose_name_plural = "Tipos de Vivienda"

    def __str__(self):
        return str(self.housing_type_name)


class Nomenclature(models.Model):
    nomenclature_name = models.CharField(
        verbose_name="Nombre de Nomenclatura", max_length=45
    )

    class Meta:
        verbose_name = "Nomenclatura"
        verbose_name_plural = "Nomenclaturas"

    def __str__(self):
        return str(self.nomenclature_name)


class HousingUnit(models.Model):
    id_housing_type = models.ForeignKey(
        HousingType, on_delete=CASCADE, verbose_name="Tipo Vivienda"
    )
    id_admin = models.ForeignKey(
        AdminAccount, on_delete=CASCADE, verbose_name="Administrador"
    )
    id_nomenclature = models.ForeignKey(
        Nomenclature, on_delete=CASCADE, verbose_name="Nomenclatura"
    )
    complement = models.CharField(verbose_name="Complemento", max_length=5)
    nomenclature = models.CharField(verbose_name="Nomenclatura", max_length=45)
    delivery_date = models.DateField(verbose_name="Fecha de Entrega")
    status = models.CharField(verbose_name="Estado", max_length=40)

    class Meta:
        verbose_name = "Unidad Habitacional"
        verbose_name_plural = "Unidades Habitacionales"

    def __str__(self):
        return str(self.nomenclature)


class HabitantDetail(models.Model):
    id_housing_unit = models.ForeignKey(
        HousingUnit, on_delete=CASCADE, verbose_name="Unidad Habitacional"
    )
    id_user = models.ForeignKey(User, on_delete=CASCADE, verbose_name="Usuario")
    admission_date = models.DateTimeField(verbose_name="Fecha de Ingreso")
    retirement_date = models.DateTimeField(verbose_name="Fecha de Retiro")

    class Meta:
        verbose_name = "Detalle Habitante"
        verbose_name_plural = "Detalle Habitantes"

    def __str__(self):
        return str(self.id_user)
