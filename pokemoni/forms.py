from django import forms

from .models import Trener

class TreningForm(forms.Form):
    trener_meno = forms.ModelChoiceField(queryset=Trener.objects.filter(vMeste=True), label='Meno trénera')

    pokemon_id = forms.IntegerField(label='ID pokémona')
