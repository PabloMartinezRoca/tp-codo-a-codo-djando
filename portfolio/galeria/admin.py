from django.contrib import admin
from .models import Proyecto

# Register your models here.


class AdminGaleria(admin.ModelAdmin):
    # agrega los siguientes campos, en modo solo lectura
    readonly_fields = ('creado', 'actualizado')


admin.site.register(Proyecto, AdminGaleria)
