
from django import forms

class UnitInfoForm(forms.Form):
    unit_serial_number = forms.CharField(
                            max_length=50,
                            widget=forms.TextInput(attrs={
                                'placeholder': 'Serial number',
                            }),
                            required=True)


from django.forms import ModelForm
from models import UnitInfo

class UnitInfoForm(ModelForm):
    class Meta:
        model = UnitInfo.Post

