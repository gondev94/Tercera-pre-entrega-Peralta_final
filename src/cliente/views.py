from django.shortcuts import render, redirect
from .models import Cliente, Carrito, Producto
from .forms import ClienteForm, CarritoForm, ProductoForm

def index(request):
    return render(request, "cliente/index.html")

def about(request):
    return render(request, "about/index.html")

def cliente_list(request):
    query = Cliente.objects.all()
    contex = {"object_list": query}
    return render(request, "cliente/cliente_list.html", contex)

def cliente_create(request):
    if request.method == "GET":
        form = ClienteForm()
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:curso_list")
    return render(request, "cliente/cliente_form.html", {"form" : form})

def carrito_list(request):
    query = Carrito.objects.all()
    contex = {"object_list": query }
    return render(request, "cliente/carrito_list.html", contex)

def carrito_create(request):
    if request.method == "GET":
        form = CarritoForm()
    if request.method == "POST":
        form = CarritoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:cliente_list")
    return render(request, "cliente/carrito_form.html", {"form" : form})

def producto_list(request):
    query = Producto.objects.all()
    contex = {"object_list": query}
    return render(request, "cliente/producto_list.html", contex)

def producto_create(request):
    if request.method == "GET":
        form = ProductoForm()
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:producto_list")
    return render(request, "cliente/producto_form.html", {"form" : form})
