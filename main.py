import json

tapahtumat = []

#Ohjelman ensimmäinen ja toiminnalle tärkein toiminto on lisätä maksutapahtumia. Append-toiminto tallentaa jokaisen lisätyn tiedon lokaaliin tiedostoon.
def lisää_tapahtuma():
    nimi = input("Syötä tapahtuman nimi: ")
    päivämäärä = input("Syötä tapahtuman päivämäärä (PP.KK.VVVV): ")
    try:
        päivämäärä = päivämäärä.split('.')
        päivä = int(päivämäärä[0])
        kuukausi = int(päivämäärä[1])
        vuosi = int(päivämäärä[2])
    except (ValueError, IndexError):
        print("Virheellinen päivämäärä. Syötä päivämäärä muodossa PP.KK.VVVV.")
        return

    määrä = input("Syötä tapahtuman määrä: ")
    try:
        määrä = float(määrä)
    except ValueError:
        print("Virheellinen määrä. Älä käytä pilkkua.")
        return

    tapahtumat.append({"nimi": nimi, "päivämäärä": päivämäärä, "määrä": määrä})
    tallenna_tapahtumat()

#Tiedot tapahtumista tallentuvat tekstitiedostoon.
def tallenna_tapahtumat():
    with open("tapahtumat.txt", "w") as tiedosto:
        json.dump(tapahtumat, tiedosto)

#Ohjelman avatessa, tiedot haetaan kyseisestä tekstitiedostosta.
def lataa_tapahtumat():
    try:
        with open("tapahtumat.txt", "r") as tiedosto:
            tapahtumat.extend(json.load(tiedosto))
    except FileNotFoundError:
        print("Tiedostoa 'tapahtumat.txt' ei löytynyt. Luodaan uusi tiedosto.")

#Taustalla ohjelmassa lasketaan käyttäjän saldoa, eli kaikkien maksutapahtumien summa tai erotus.
def laske_saldo():
    saldo = 0
    for tapahtuma in tapahtumat:
        saldo += tapahtuma["määrä"]
    return saldo

#Toinen toiminto listaa kaikki käyttäjän lisäämät maksutapahtumat peräkkäin. Ne järjestyvät datetime-importin avulla päivämäärän mukaan.
from datetime import datetime

def näytä_tapahtumat():
    järjestetyt_tapahtumat = sorted(tapahtumat, key=lambda x: datetime.strptime('-'.join(x['päivämäärä']), '%d-%m-%Y'))
    for tapahtuma in järjestetyt_tapahtumat:
        print(f"{tapahtuma['päivämäärä']} - {tapahtuma['nimi']}: {tapahtuma['määrä']}")

#Kolmas toiminto on näyttää saldon, jonka laske_saldo laskee taustalla.
def näytä_saldo():
    saldo = laske_saldo()
    if saldo > 0:
        print(f"Saldo: +{saldo}")
    elif saldo < 0:
        print(f"Saldo: {saldo}")
    else:
        print("Saldo: 0")

# Lataa tallennetut tapahtumat tiedostosta ohjelman avattaessa
lataa_tapahtumat()

#Tervetuloa-viesti, joka tulostuu vain ohjelman aloittaessa.
print("")
print("########################################")
print("####  Tervetuloa finanssilaskuriin  ####")
print("########################################")
print("")

#Luodaan True-silmukka, jotta saadaan ohjelma pyörimään kunnes toisin pyydetään.
while True:
    print("      ----------------------------      ")
    print("      |  1. Lisää tapahtuma      |      ")
    print("      |  2. Näytä tapahtumat     |      ")
    print("      |   3. Näytä saldo         |      ")
    print("      |    4.  Lopeta            |      ")
    print("      ----------------------------      ")
    print("")
    valinta = input("Syötä valintasi: ")
    print("----------------")

    if valinta == "1":
        lisää_tapahtuma()
    elif valinta == "2":
        näytä_tapahtumat()
    elif valinta == "3":
        näytä_saldo()
    elif valinta == "4":
        tallenna_tapahtumat()  # Tallenna tapahtumat tiedostoon ennen ohjelman sulkemista
        break