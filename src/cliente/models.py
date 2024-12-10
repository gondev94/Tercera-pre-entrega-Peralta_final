from django.db import models

class Cliente(models.Model):
    dni = models.PositiveIntegerField()
    nombre = models.CharField(max_length=255, unique=True)
    apellido = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido} - E-Mail: {self.email}"
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
   
    def __str__(self):
        return f"{self.nombre} -  $ {self.precio}"

class Carrito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, related_name="carritos")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_entrega = models.DateField(null=True, blank=True,)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} - Cliente: {self.cliente.nombre}"

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
    
