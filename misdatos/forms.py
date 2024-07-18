from django import forms
from misdatos.moduls import*  # Asegúrate de que el modelo esté correctamente importado


class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.IntegerField(required=True)
    email = forms.EmailField(label="Email", required=False)
    Descuentos = (
        (1, "HotSale"),
        (2, "TardesDeCafe"),
        (3, "SuperPromoSaleCafe"),
    )
    show = forms.ChoiceField(label="Turno elegido", choices=Descuentos, required=True)
    aplicado = forms.BooleanField()
    
    

    
