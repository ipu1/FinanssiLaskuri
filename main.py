import json

tapahtumat = []

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
        print("Virheellinen määrä. Syötä määrä numerona.")
        return

    tapahtumat.append({"nimi": nimi, "päivämäärä": päivämäärä, "määrä": määrä})
    tapahtumat.sort(key=lambda x: x["päivämäärä"])  # Lajittele tapahtumat päivämäärän perusteella
    tallenna_tapahtumat()

def tallenna_tapahtumat():
    with open("tapahtumat.txt", "w") as tiedosto:
        json.dump(tapahtumat, tiedosto)

def lataa_tapahtumat():
    try:
        with open("tapahtumat.txt", "r") as tiedosto:
            tapahtumat.extend(json.load(tiedosto))
    except FileNotFoundError:
        print("Tiedostoa 'tapahtumat.txt' ei löytynyt. Luodaan uusi tiedosto.")

def laske_saldo():
    saldo = 0
    for tapahtuma in tapahtumat:
        saldo += tapahtuma["määrä"]
    return saldo

def näytä_tapahtumat():
    for tapahtuma in tapahtumat:
        print(f"{tapahtuma['päivämäärä']} - {tapahtuma['nimi']}: {tapahtuma['määrä']}")

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

while True:
    print("1. Lisää tapahtuma")
    print("2. Näytä tapahtumat")
    print("3. Näytä saldo")
    print("4. Lopeta")

    valinta = input("Syötä valintasi: ")

    if valinta == "1":
        lisää_tapahtuma()
    elif valinta == "2":
        näytä_tapahtumat()
    elif valinta == "3":
        näytä_saldo()
    elif valinta == "4":
        tallenna_tapahtumat()  # Tallenna tapahtumat tiedostoon ennen ohjelman sulkemista
        break