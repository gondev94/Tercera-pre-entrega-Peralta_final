from django.db import models

class Cliente(models.Model):
    dni = models.IntegerField(max_length=10)
    nombre = models.CharField(max_length=255, unique=True)
    apellido = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.email}"
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

class Carrito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Carrito de {self.cliente.nombre}: {self.producto.nombre} x {self.cantidad}"

    def total_precio(self):
        return self.cantidad * self.producto.precio
    
    def listar_carrito(self):
        carrito = self.carritos.all()  # Obtiene los productos del carrito del cliente
        if carrito:
            return [{"producto": item.producto.nombre, "precio": item.producto.precio, "cantidad": item.cantidad} for item in carrito]
        return "El carrito está vacío."
    
    def realizar_compra(self):
        carrito = self.carritos.all()
        if not carrito:
            return "El carrito está vacío, no se puede realizar la compra."

        total = sum(item.total_precio() for item in carrito)
        detalle = [{"producto": item.producto.nombre, "precio": item.producto.precio, "cantidad": item.cantidad} for item in carrito]

        # Vaciar el carrito tras la compra
        carrito.delete()

        return {"total": total, "detalle": detalle}