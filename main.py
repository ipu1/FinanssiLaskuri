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

# Create the main window
window = tk.Tk()
window.title("Tapahtumahallinta")

# Create and configure the input fields
nimi_label = tk.Label(window, text="Tapahtuman nimi:")
nimi_label.grid(row=0, column=0, padx=5, pady=5)
nimi_input = tk.Entry(window)
nimi_input.grid(row=0, column=1, padx=5, pady=5)

päivämäärä_label = tk.Label(window, text="Päivämäärä (VVVV-KK-PP):")
päivämäärä_label.grid(row=1, column=0, padx=5, pady=5)
päivämäärä_input = tk.Entry(window)
päivämäärä_input.grid(row=1, column=1, padx=5, pady=5)

määrä_label = tk.Label(window, text="Määrä:")
määrä_label.grid(row=2, column=0, padx=5, pady=5)
määrä_input = tk.Entry(window)
määrä_input.grid(row=2, column=1, padx=5, pady=5)

# Create the buttons
lisää_button = tk.Button(window, text="Lisää", command=lisää_tapahtuma)
lisää_button.grid(row=3, column=0, padx=5, pady=5)

näytä_button = tk.Button(window, text="Näytä", command=näytä_tapahtumat)
näytä_button.grid(row=3, column=1, padx=5, pady=5)

# Create and configure the search options
haku_tyyppi_label = tk.Label(window, text="Hae:")
haku_tyyppi_label.grid(row=4, column=0, padx=5, pady=5)
haku_tyyppi_valinta = tk.StringVar(window)
haku_tyyppi_valinta.set("nimi")
haku_tyyppi_menu = tk.OptionMenu(window, haku_tyyppi_valinta, "nimi", "päivämäärä")
haku_tyyppi_menu.grid(row=4, column=1, padx=5, pady=5)

haku_kysely_label = tk.Label(window, text="Hakusana:")
haku_kysely_label.grid(row=5, column=0, padx=5, pady=5)
haku_kysely_input = tk.Entry(window)
haku_kysely_input.grid(row=5, column=1, padx=5, pady=5)

hae_button = tk.Button(window, text="Hae", command=hae_tapahtumat)
hae_button.grid(row=6, column=0, padx=5, pady=5)

# Create the text widget to display the events
tapahtumat_text = tk.Text(window)
tapahtumat_text.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

# Start the main loop
window.mainloop()