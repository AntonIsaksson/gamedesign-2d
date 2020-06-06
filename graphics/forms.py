from django import forms
from .models import AllItems

class ItemOrderForm(forms.ModelForm):

    class Meta:
        model = AllItems
        fields = ['category', 'color', 'text_content']
    
    # def send_email(self):