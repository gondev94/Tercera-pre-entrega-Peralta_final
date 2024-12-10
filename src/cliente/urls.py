from django.urls import path
from .views import index, about, cliente_list, carrito_list, producto_list

app_name = "cliente"

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("cliente/list/", cliente_list, name="cliente_list"),
    path("producto/list/", producto_list, name="producto_list"),
    path("carrito/list", carrito_list, name="carrito_list"),
]