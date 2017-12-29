from django.shortcuts import render

from django.http import HttpResponseRedirect

from django.shortcuts import reverse

from .models import Pokemon, Trener, Kurz, Druzinka, Ucet

from .forms import TreningForm, ObchodForm

def trening(request):
    template_name = 'pokemoni/trening.html'
    form = TreningForm()

    if request.method == 'POST':
        try:
            trener = Trener.objects.get(pk=request.POST['trener_meno'])

        except (KeyError, ValueError, Trener.DoesNotExist):
            return render(request, template_name, {'form': form, 'error_message': 'Tréner neexistuje'})

        try:
            pokemon = Pokemon.objects.get(pk=request.POST['pokemon_id'])

        except (KeyError, ValueError, Pokemon.DoesNotExist):
            return render(request, template_name, {'form': form, 'error_message': 'Pokémon neexistuje'})

        if not hasattr(pokemon.idDruzinka, 'ucet') or pokemon.idDruzinka.ucet.peniaze < trener.cena:
            return render(request, template_name, {'form': form, 'error_message': 'Družinka nemá dosť peňazí'})

        if pokemon.energia < 5:
            return render(request, template_name, {'form': form, 'error_message': 'Pokémon je vyčerpaný'})

        pokemon.sila += trener.qSila
        pokemon.rychlost += trener.qRychlost
        pokemon.postreh += trener.qPostreh
        pokemon.odolnost += trener.qOdolnost
    
        pokemon.energia += -5
        pokemon.idDruzinka.ucet.peniaze -= trener.cena

        kurz = Kurz(idTrener=trener, idPokemon=pokemon)
        kurz.save()

        pokemon.idDruzinka.ucet.save()
        pokemon.save()

        return HttpResponseRedirect(reverse('pokemoni:trening'))

    else:
        return render(request, template_name, {'form': form})

def obchod(request):
    template_name = 'pokemoni/obchod.html'
    form = ObchodForm()

    if request.method == 'POST':
        try:
            druzinka = Druzinka.objects.get(pk=request.POST['nova_druzinka'])

        except (KeyError, ValueError, Druzinka.DoesNotExist):
            return render(request, template_name, {'form': form, 'error_message': 'Družinka neexistuje'})

        try:
            pokemon = Pokemon.objects.get(pk=request.POST['pokemon_id'])

        except (KeyError, ValueError, Pokemon.DoesNotExist):
            return render(request, template_name, {'form': form, 'error_message': 'Pokémon neexistuje'})

        pokemon.idDruzinka = druzinka
        pokemon.nazov = request.POST['novy_nazov'] if request.POST['novy_nazov'] != '' else pokemon.nazov

        pokemon.save()

        return HttpResponseRedirect(reverse('pokemoni:obchod'))

    else:
        return render(request, template_name, {'form': form})

def prehlad(request):
    template_name = 'pokemoni/prehlad.html'
    ucty = Ucet.objects.all().order_by('-popularita')
    druzinky = Druzinka.objects.all()
    treneri = Trener.objects.filter(vMeste=True)
    return render(request, template_name, {'ucty': ucty, 'druzinky': druzinky, 'treneri': treneri})
