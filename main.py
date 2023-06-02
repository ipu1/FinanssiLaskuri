import csv
import tkinter as tk
from tkinter import messagebox

tapahtumat = []

def lisää_tapahtuma():
    nimi = nimi_input.get()
    päivämäärä = päivämäärä_input.get()
    määrä = määrä_input.get()

    if nimi and päivämäärä and määrä:
        tapahtumat.append({"nimi": nimi, "päivämäärä": päivämäärä, "määrä": määrä})
        messagebox.showinfo("Lisää tapahtuma", "Tapahtuma lisätty onnistuneesti!")
        nimi_input.delete(0, tk.END)
        päivämäärä_input.delete(0, tk.END)
        määrä_input.delete(0, tk.END)
    else:
        messagebox.showerror("Virhe", "Täytä kaikki kentät.")

def näytä_tapahtumat():
    tapahtumat_text.delete("1.0", tk.END)
    for tapahtuma in tapahtumat:
        tapahtumat_text.insert(tk.END, f"{tapahtuma['päivämäärä']} - {tapahtuma['nimi']}: {tapahtuma['määrä']}\n")

def hae_tapahtumat():
    haku_tyyppi = haku_tyyppi_valinta.get()
    haku_kysely = haku_kysely_input.get()

    tapahtumat_text.delete("1.0", tk.END)

    for tapahtuma in tapahtumat:
        if tapahtuma[haku_tyyppi] == haku_kysely:
            tapahtumat_text.insert(tk.END, f"{tapahtuma['päivämäärä']} - {tapahtuma['nimi']}: {tapahtuma['määrä']}\n")

while True:
    print("1. Lisää tapahtuma")
    print("2. Näytä tapahtumat")
    print("3. Hae tapahtumia")
    print("4. Lopeta")

    valinta = input("Syötä valintasi: ")

# Start the main loop
window.mainloop()