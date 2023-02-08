from django.db import models
from datetime import date
# From models
from polls.models import Period
from unit.models import AdminAccount
from django.db.models.deletion import CASCADE

# Create your models here.

class Month(models.Model):
    mounth_name = models.CharField(verbose_name = 'Nombre de Mes', max_length = 20)
    # Atributos de Auditoria:
    create_at = models.DateField(auto_now = False, auto_now_add = True, verbose_name = "Fecha de creación", null = True, blank = True) 
    modify_at = models.DateField(auto_now = True, auto_now_add = False, verbose_name = "Fecha de actualización", null = True, blank = True)

    class Meta:
        verbose_name = 'Mes de Periodo'
        verbose_name_plural = 'Meses de periodo'
    
    def __str__(self):
        return f'{self.mounth_name}'

class Category(models.Model):
    category_name = models.CharField(verbose_name ='Categoría', max_length = 50)
    # Atributos de Auditoria:
    create_at = models.DateField(auto_now = False, auto_now_add = True, verbose_name = "Fecha de creación", null = True, blank = True) 
    modify_at = models.DateField(auto_now = True, auto_now_add = False, verbose_name = "Fecha de actualización", null = True, blank = True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias de Presupuesto'
    
    def __str__(self):
        return f'{self.category_name}'

class Concept(models.Model):
    user = models.ForeignKey(AdminAccount, on_delete = CASCADE)
    category = models.ForeignKey(Category, on_delete = CASCADE)
    concept = models.CharField(verbose_name ='Nombre de Concepto', max_length = 50)
    # Atributos de Auditoria:
    create_at = models.DateField(auto_now = False, auto_now_add = True, verbose_name = "Fecha de creación", null = True, blank = True) 
    modify_at = models.DateField(auto_now = True, auto_now_add = False, verbose_name = "Fecha de actualización", null = True, blank = True)

    class Meta:
        verbose_name = 'Concepto'
        verbose_name_plural = 'Conceptos de Presupuesto'
    
    def __str__(self):
        return f'{self.concept}'

class Movement(models.Model):
    admin_user = models.ForeignKey(AdminAccount, on_delete = CASCADE)
    period = models.ForeignKey(Period, on_delete = CASCADE)
    mounth = models.ForeignKey(Mounth, on_delete = CASCADE)
    category = models.ForeignKey(Category, on_delete = CASCADE)
    concept = models.ForeignKey(Concept, on_delete = CASCADE)
    movement_value = models.DecimalField(verbose_name='Valor Presupuestado', max_digits=20, decimal_places=2)
    movement_note = models.CharField(verbose_name='Notas de Movimiento', max_length=256, default='N/A')
    # Atributos de Auditoria:
    create_at = models.DateField(auto_now = False, auto_now_add = True, verbose_name = "Fecha de creación", null = True, blank = True) 
    modify_at = models.DateField(auto_now = True, auto_now_add = False, verbose_name = "Fecha de actualización", null = True, blank = True)

    class Meta:
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'
    
    def __str__(self):
        return f'{self.concept}'

class Budget(models.Model):
    admin_user = models.ForeignKey(AdminAccount, on_delete =CASCADE)
    period = models.ForeignKey(Period, on_delete =CASCADE)
    mounth = models.ForeignKey(Mounth, on_delete =CASCADE)
    category = models.ForeignKey(Category, on_delete =CASCADE)
    concept = models.ForeignKey(Concept, on_delete =CASCADE)
    budget_value = models.DecimalField(verbose_name='Valor Presupuestado', max_digits = 20, decimal_places = 2)
    budget_notes = models.CharField(verbose_name='Notas de Presupuesto', max_length=256, default='N/A')
    # Atributos de Auditoria:
    create_at = models.DateField(auto_now = False, auto_now_add = True, verbose_name = "Fecha de creación", null = True, blank = True) 
    modify_at = models.DateField(auto_now = True, auto_now_add = False, verbose_name = "Fecha de actualización", null = True, blank = True)

    class Meta:
        verbose_name = 'Presupuesto'
        verbose_name_plural = 'Presupuesto del Año'
    
    def __str__(self):
        return f'{self.period} {self.mounth} {self.concept}'

