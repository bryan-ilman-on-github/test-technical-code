from django import forms
from .models import AngkaModel


class AngkaForm(forms.ModelForm):
    class Meta:
        model = AngkaModel
        fields = ["masukan"]

    masukan = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Input Angka'}))
