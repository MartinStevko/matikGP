from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

import time
from random import randint, uniform

from .models import Pokemon, Trener, Kurz, Druzinka, Ucet, Akcia
from .forms import TreningForm, ObchodForm, JedalenForm, SpravcaForm

def bezi():
    z = zaciatok()
    k = koniec()
    t = round(time.time())
    if z < t and t < k:
        return True
    else:
        return False

def trening(request):
    template_name = 'pokemoni/trening.html'
    form = TreningForm()
    be = bezi()

    if request.method == 'POST':
        try:
            trener = Trener.objects.get(pk=request.POST['trener_meno'])

        except (KeyError, ValueError, Trener.DoesNotExist):
            return render(request, template_name, {'be': be, 'form': form, 'error_message': 'Tréner neexistuje'})

        try:
            pokemon = Pokemon.objects.get(pk=request.POST['pokemon_id'])

        except (KeyError, ValueError, Pokemon.DoesNotExist):
            return render(request, template_name, {'be': be, 'form': form, 'error_message': 'Pokémon neexistuje'})

        if not hasattr(pokemon.idDruzinka, 'ucet') or pokemon.idDruzinka.ucet.peniaze < trener.cena:
            return render(request, template_name, {'be': be, 'form': form, 'error_message': 'Družinka nemá dosť peňazí'})

        if pokemon.energia < 5:
            return render(request, template_name, {'be': be, 'form': form, 'error_message': 'Pokémon je vyčerpaný'})

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
        return render(request, template_name, {'be': be, 'form': form})

def obchod(request):
    template_name = 'pokemoni/obchod.html'
    form = ObchodForm()
    be = bezi()

    if request.method == 'POST':
        try:
            druzinka = Druzinka.objects.get(pk=request.POST['nova_druzinka'])

        except (KeyError, ValueError, Druzinka.DoesNotExist):
            return render(request, template_name, {'be': be, 'form': form, 'error_message': 'Družinka neexistuje'})

        try:
            pokemon = Pokemon.objects.get(pk=request.POST['pokemon_id'])

        except (KeyError, ValueError, Pokemon.DoesNotExist):
            return render(request, template_name, {'be': be, 'form': form, 'error_message': 'Pokémon neexistuje'})

        pokemon.idDruzinka = druzinka
        pokemon.nazov = request.POST['novy_nazov'] if request.POST['novy_nazov'] != '' else pokemon.nazov

        pokemon.save()

        return HttpResponseRedirect(reverse('pokemoni:obchod'))

    else:
        return render(request, template_name, {'be': be, 'form': form})

def jedalen(request):
    template_name = 'pokemoni/jedalen.html'
    form = JedalenForm()
    be = bezi()

    if request.method == 'POST':
        try:
            pokemon = Pokemon.objects.get(pk=request.POST['pokemon_id'])

        except (KeyError, ValueError, Pokemon.DoesNotExist):
            return render(request, template_name, {'be': be, 'form': form, 'error_message': 'Pokémon neexistuje'})

        if not hasattr(pokemon.idDruzinka, 'ucet') or pokemon.idDruzinka.ucet.peniaze < 5:
            return render(request, template_name, {'be': be, 'form': form, 'error_message': 'Družinka nemá dosť peňazí'})

        pokemon.jedol = True
        pokemon.idDruzinka.ucet.peniaze -= 5

        pokemon.save()
        pokemon.idDruzinka.ucet.save()

        return HttpResponseRedirect(reverse('pokemoni:jedalen'))

    else:
        return render(request, template_name, {'be': be, 'form': form})

def zaciatok(t = 10**11):
    if t != 10**11:
        global zaciatok_cas
        zaciatok_cas = round(t)
        with open('setup/zaciatok.txt', 'w') as f:
            f.write(str(zaciatok_cas))
    try:
        with open('setup/zaciatok.txt', 'r') as f:
            t = int(f.readline())
    except(ValueError, FileNotFoundError):
        t = 10**11
    return t

def koniec(t = 10**11):
    if t != 10**11:
        global koniec_cas
        koniec_cas = zaciatok()+(((t-zaciatok())//480)+1)*480
        with open('setup/koniec.txt', 'w') as f:
            f.write(str(round(koniec_cas)))
    try:
        with open('setup/koniec.txt', 'r') as f:
            t = int(f.readline())
    except(ValueError, FileNotFoundError):
        t = 10**11
    return t

# alert("Cas vyprsal!");
def timer():
    zaciatok_hry = zaciatok()
    koniec_hry = koniec()
    teraz = round(time.time())
    if zaciatok_hry < teraz:
        if teraz < koniec_hry:
            t = 480 - ((teraz - zaciatok_hry) % 480) # modulo 60 * dlzka kola v minutach
            m = t // 60
            s = t % 60
        else:
            m, s = 0, -1
    else:
        m, s = -1, 0
    return m, s

def spravca(request):
    template_name = 'pokemoni/spravca.html'
    form = SpravcaForm()
    akcie = Akcia.objects.all()
    k = round((time.time() - zaciatok()) // 480) + 1
    mi, se = timer()

    if request.method == 'POST':
        akcia = str(request.POST['akcia'])
        # 1 - Začni hru
        # 2 - Ukonči hru
        # 3 - Vyhodnoť kolo
        if akcia == '1':
            message = 'Hra začala'
            zaciatok(time.time())
            with open('setup/koniec.txt', 'w') as f:
                f.write('')
        elif akcia == '2':
            message = 'Hra skončí po konci tohto kola (akcia sa odvráti jedine premazaním súboru koniec.txt)'
            koniec(time.time())
        elif akcia == '3':
            message = "Kolo %d bolo vyhodnotené" % (k)
            pokemoni = Pokemon.objects.all()

            sutaz = []

            for pokemon in pokemoni:
                if not hasattr(pokemon.idDruzinka, 'ucet'):
                    continue
                elif not pokemon.jedol:
                    pokemon.idDruzinka = Druzinka.objects.get(nazov='Mrtvoly')
                else:
                    sutaz.append((skore(pokemon), pokemon))
                    pokemon.jedol = False
                    pokemon.energia = min(10, pokemon.energia+2)

                pokemon.save()

            sutaz.sort(reverse=True)

            for i in range(len(sutaz)):
                sutaz[i][1].idDruzinka.ucet.popularita += round(100-((i+1)**2)/50)
                sutaz[i][1].idDruzinka.ucet.peniaze += round((100-i)**2/50)

                sutaz[i][1].idDruzinka.ucet.save()

            treneri = Trener.objects.all()

            for trener in treneri:
                if randint(1, 7) == 4:
                    trener.vMeste = True
                else:
                    trener.vMeste = False

                trener.save()

        else:
            message = 'Akcia '+str(akcia)+' sa nevykonala'
            return render(request, template_name, {'mi': mi, 'se': se, 'kolo': k, 'akcie': akcie, 'form': form, 'message': message})

        return render(request, template_name, {'mi': mi, 'se': se, 'kolo': k, 'akcie': akcie, 'form': form, 'message': message})
    else:
        return render(request, template_name, {'mi': mi, 'se': se, 'kolo': k, 'form': form, 'akcie': akcie})

def prehlad(request):
    template_name = 'pokemoni/prehlad.html'
    ucty = Ucet.objects.all().order_by('-popularita')
    druzinky = Druzinka.objects.all()
    treneri = Trener.objects.filter(vMeste=True)
    return render(request, template_name, {'ucty': ucty, 'druzinky': druzinky, 'treneri': treneri})

def druzinka(request, num):
    template_name = 'pokemoni/druzinka.html'
    druz = Druzinka.objects.get(url_number=num)
    pokemoni = Pokemon.objects.filter(idDruzinka=druz.id)
    ucet = Ucet.objects.get(idDruzinka=druz.id)
    mi, se = timer()
    return render(request, template_name, {'m': mi, 's': se, 'druz': druz, 'pokemoni': pokemoni, 'ucet': ucet})

def zoznam(request):
    template_name = 'pokemoni/zoznam.html'
    druzinky = Druzinka.objects.all()
    return render(request, template_name, {'druzinky': druzinky})

def skore(p):
    return p.sila**3*p.rychlost**4*p.postreh**3.5*p.odolnost**2.5*uniform(0.95, 1.05)
