from django.shortcuts import render

from .models import Pokemon, Trener, Kurz

from .forms import TreningForm

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

        return render(request, template_name, {'form': form, 'error_message': 'Tréning prebehol v poriadku'})

    else:
        return render(request, template_name, {'form': form})
