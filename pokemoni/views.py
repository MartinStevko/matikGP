from django.shortcuts import render, get_object_or_404

from django.views import generic

from django.http import HttpResponseRedirect

from django.urls import reverse

from .models import Pokemon, Trener

class TreningView(generic.base.TemplateView):
    template_name = "pokemoni/trening.html"

def trenuj(request):
    try:
        trener = Trener.objects.get(pk=request.POST['trener_id'])
    except (KeyError, Trener.DoesNotExist):
        return render(request, 'pokemoni/trening.html', {'error_message': 'Tréner neexistuje'})

    try:
        pokemon = Pokemon.objects.get(pk=request.POST['pokemon_id'])
    except (KeyError, Pokemon.DoesNotExist):
        return render(request, 'pokemoni/trening.html', {'error_message': 'Pokémon neexistuje'})

    pokemon.sila += trener.qSila
    pokemon.rychlost += trener.qRychlost
    pokemon.postreh += trener.qPostreh
    pokemon.odolnost += trener.qOdolnost

    pokemon.save()

    return HttpResponseRedirect(reverse('pokemoni:trening'))
