from django import forms
from .models import Cliente, Producto, Carrito


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        
class CarritoForm(forms.ModelForm):
    class Meta:
        model = Carrito
        fields = "__all__"
        widgets = {"fecha_entrega": forms.DateInput(attrs={"type": "date"}),
            
        }
        
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"