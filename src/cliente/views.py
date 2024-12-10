from django.shortcuts import render
from .models import Cliente, Carrito, Producto
# Create your views here.
def index(request):
    return render(request, "cliente/index.html")

def about(request):
    return render(request, "about/index.html")

def cliente_list(request):
    query = Cliente.objects.all()
    contex = {"object_list": query}
    return render(request, "cliente/cliente_list.html", contex)

def carrito_list(request):
    query = Carrito.objects.all()
    contex = {"object_list": query }
    return render(request, "cliente/carrito_list.html", contex)

def producto_list(request):
    query = Producto.objects.all()
    contex = {"object_list": query}
    return render(request, "cliente/producto_list.html", contex)

