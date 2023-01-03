from django.db import models

# Create your models here.


class Proyecto(models.Model):
    titulo = models.CharField(
        max_length=200, verbose_name='Título del proyecto')
    descripcion = models.TextField(
        verbose_name='Descripción (Máx. 255 caracteres)')
    # path desde la raíz del proyecto. Si la carpeta no existiese, la crea.
    imagen = models.ImageField(
        upload_to='galeria/imagenes/proyectos/', verbose_name='Imagen del proyecto')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    # campo agregado posteriormente al modelo
    link = models.URLField(verbose_name='Hiperevínculo', blank=True, null=True)

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        # orden de listado. en este caso de más nuevo a más viejo
        ordering = ['-creado']

    # Devuelve el nombre del proyecto para aplicarlo en la lista de proyectos en lugar del nombre de la instacia ('Proyecto object(n)')
    def __str__(self) -> str:
        return self.titulo
