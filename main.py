import csv

tapahtumat = []

def lisää_tapahtuma():
    nimi = input("Syötä tapahtuman nimi: ")
    päivämäärä = input("Syötä tapahtuman päivämäärä (VVVV-KK-PP): ")
    määrä = float(input("Syötä tapahtuman määrä: "))
    tapahtumat.append({"nimi": nimi, "päivämäärä": päivämäärä, "määrä": määrä})

def näytä_tapahtumat():
    for tapahtuma in tapahtumat:
        print(f"{tapahtuma['päivämäärä']} - {tapahtuma['nimi']}: {tapahtuma['määrä']}")

def hae_tapahtumat():
    haku_tyyppi = input("Hae nimellä vai päivämäärällä? ")
    haku_kysely = input(f"Syötä {haku_tyyppi} haettavaksi: ")

    for tapahtuma in tapahtumat:
        if tapahtuma[haku_tyyppi] == haku_kysely:
            print(f"{tapahtuma['päivämäärä']} - {tapahtuma['nimi']}: {tapahtuma['määrä']}")

while True:
    print("Tervetuloa finanssilaskuriin")
    print("")
    print("1. Lisää tapahtuma")
    print("2. Näytä tapahtumat")
    print("3. Hae tapahtumia")
    print("4. Lopeta")

    valinta = input("Syötä valintasi: ")

    if valinta == "1":
        lisää_tapahtuma()
    elif valinta == "2":
        näytä_tapahtumat()
    elif valinta == "3":
        hae_tapahtumat()
    elif valinta == "4":
        break