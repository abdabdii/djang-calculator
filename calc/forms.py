from django.forms import ModelForm,Select,NumberInput
from .models import Calculation

class CalcForm(ModelForm):
    class Meta:
        model = Calculation
        fields = ['number1','operation','number2']
        widgets = {
            'number1': NumberInput(attrs={'class':'form-control'}),
            'number2': NumberInput(attrs={'class':'form-control'}),
            'operation':Select(attrs={'class':'form-control'})
        }
