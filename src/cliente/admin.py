from django.contrib import admin

from .models import Cliente, Producto, Carrito

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'apellido', 'email')  # Campos visibles en la lista
    search_fields = ('dni', 'nombre', 'apellido', 'email')  # Campos por los que se puede buscar
    list_filter = ('apellido',)  # Filtros para facilitar la búsqueda
    ordering = ('apellido', 'nombre')  # Orden predeterminado

# Configuración para el modelo Producto
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')  # Mostrar nombre y precio y cantidad 
    search_fields = ('nombre',)  # Habilitar búsqueda por nombre
    list_filter = ('precio',)  # Filtro por rango de precios
    ordering = ('nombre',)  # Orden alfabético por nombre

# Configuración para el modelo Carrito
@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'producto', 'cantidad', 'total_precio')  # Mostrar cliente, producto, cantidad y total
    search_fields = ('cliente__nombre', 'producto__nombre')  # Búsqueda por cliente o producto
    list_filter = ('cliente', 'producto')  # Filtrar por cliente o producto

    # Método para calcular el precio total
    @admin.display(description="Precio total")
    def total_precio(self, obj):
        return obj.total_precio()
    