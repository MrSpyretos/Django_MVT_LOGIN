from django import forms
from .models import Lender
class LenderCreate(forms.ModelForm):
    class Meta:
        model = Lender
        fields = '__all__'