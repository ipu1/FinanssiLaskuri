import csv

tapahtumat = []

def lisää_tapahtuma():
    nimi = input("Syötä tapahtuman nimi: ")
    päivämäärä = int(input("Syötä tapahtuman päivämäärä (PP.KK.VVVV): "))
    määrä = float(input("Syötä tapahtuman määrä: "))
    tapahtumat.append({"nimi": nimi, "päivämäärä": päivämäärä, "määrä": määrä})

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
        break