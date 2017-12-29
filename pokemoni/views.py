from django.shortcuts import render

from django.views import generic

from django.http import HttpResponseRedirect

from django.urls import reverse

from .models import Pokemon, Trener

from .forms import TreningForm

def trening(request):
    if request.method == 'POST':
        trener = Trener.objects.get(pk=request.POST['trener_meno'])

        try:
            pokemon = Pokemon.objects.get(pk=request.POST['pokemon_id'])

<<<<<<< HEAD
        except (KeyError, ValueError, Pokemon.DoesNotExist):
            return render(request, 'pokemoni/trening.html', {'form': TreningForm(), 'error_message': 'Pokémon neexistuje'})
=======
    pokemon.sila += trener.qSila
    pokemon.rychlost += trener.qRychlost
    pokemon.postreh += trener.qPostreh
    pokemon.odolnost += trener.qOdolnost
    
    pokemon.energia += -5
>>>>>>> 23c2b027b2257425c685a2953b76c5a323f21e52

        pokemon.sila += trener.qSila
        pokemon.rychlost += trener.qRychlost
        pokemon.postreh += trener.qPostreh
        pokemon.odolnost += trener.qOdolnost
    
        pokemon.energia += -5

        pokemon.save()

        return render(request, 'pokemoni/trening.html', {'form': TreningForm(), 'error_message': 'Vyšlo to'})

    else:
        return render(request, 'pokemoni/trening.html', {'form': TreningForm()})
