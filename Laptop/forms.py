from django import forms
from . models import laptop
class LaptopForm(forms.ModelForm):
    class Meta:
        model=laptop
        fields=['brand','price','imei','color']