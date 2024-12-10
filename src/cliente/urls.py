from django.urls import path
from .views import index, about, cliente_list, carrito_list, producto_list, cliente_create, producto_create, carrito_create

app_name = "cliente"

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("cliente/list/", cliente_list, name="cliente_list"),
    path("cliente/create/", cliente_create, name="cliente_create"),
    path("producto/list/", producto_list, name="producto_list"),
    path("producto/create/", producto_create, name="producto_create"),
    path("carrito/list", carrito_list, name="carrito_list"),
    path("carrito/create/", carrito_create, name="carrito_create"),
    
]