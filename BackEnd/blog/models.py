from django.db import models

# Create your models here.
class Tags(models.Model):
    name_tag = title = models.CharField(verbose_name ='Etiqueta', max_length = 20)

    class Meta:
        verbose_name = 'Etiquetas'
    
    def __str__(self):
        return f'{self.name_tag}'

class Post(models.Model):
    user = models.ForeignKey(AdminAccount, on_delete = CASCADE, verbose_name = 'Administrador')
    title = models.CharField(verbose_name ='Titulo de la Publicación', max_length = 50)
    content = models.TextField(verbose_name = 'Contenido de la Publicación', null = True, blank = True)
    tags = models.ManyToManyField(Tags, on_delete = CASCADE, verbose_name = 'Etiquetas')
    status = models.BooleanField(verbose_name ='Estado', default = True)
    # Atributos de Auditoria:
    create_at = models.DateField(auto_now = False, auto_now_add = True, verbose_name = "Fecha de creación", null = True, blank = True) 
    modify_at = models.DateField(auto_now = True, auto_now_add = False, verbose_name = "Fecha de actualización", null = True, blank = True)

    class Meta:
        verbose_name = 'Publicaciones'

    def __str__(self):
        return f'{self.title}'


 