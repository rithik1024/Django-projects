from django import  forms 
from .models import media

class mediaform(forms.ModelForm):
    class Meta:
        model=media
        fields=["name","image"]
        