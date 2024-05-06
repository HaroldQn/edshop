from django.contrib import admin

# Register your models here.
from .models import Categoria, Producto

admin.site.register(Categoria)
#admin.site.register(Producto)

#Decorador
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    #CON ESTO PODEMOS PERSONALIZAR LA VISTA ADMIN
    list_display = ('nombre', 'precio', 'categoria', 'fecha_registro')
    list_editable = ('precio',)
