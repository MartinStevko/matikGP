from django import forms

from .models import Trener, Druzinka, Akcia

class TreningForm(forms.Form):
    trener_meno = forms.ModelChoiceField(queryset=Trener.objects.filter(vMeste=True), label='Meno trénera')

    pokemon_id = forms.IntegerField(label='ID pokémona')

class ObchodForm(forms.Form):
    nova_druzinka = forms.ModelChoiceField(queryset=Druzinka.objects.all(), label='Nová družinka')

    novy_nazov = forms.CharField(max_length=100, label='Nový názov', required=False)

    pokemon_id = forms.IntegerField(label='ID pokémona')

class JedalenForm(forms.Form):
    pokemon_id = forms.IntegerField(label='ID pokémona')

class SpravcaForm(forms.Form):
    akcia = forms.ModelChoiceField(queryset=Akcia.objects.all(), label='Akcia')
