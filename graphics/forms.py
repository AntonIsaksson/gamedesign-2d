from django import forms
from .models import Designs

class ItemOrderForm(forms.ModelForm):

    class Meta:
        model = Designs
        fields = ['category', 'color', 'text_content']
    
    # def send_email(self):