import tkinter as tk
from tkinter import ttk
from random import choice


def spin():
    global credito

    if credito >= 0.50:
        credito -= 0.50
        simboli = ["7", "BAR", "ciliegia", "limone", "arancia", "banana"]
        rullo1 = choice(simboli)
        rullo2 = choice(simboli)
        rullo3 = choice(simboli)

        rullo1_label.config(text=rullo1)
        rullo2_label.config(text=rullo2)
        rullo3_label.config(text=rullo3)

        if rullo1 == rullo2 == rullo3:
            credito += 10.0
            risultato_label.config(text="Hai vinto! Hai ora {} euro di credito.".format(credito))
        else:
            risultato_label.config(text="Riprova! Credito rimanente: {} euro.".format(credito))
    else:
        risultato_label.config(text="Credito insufficiente. Ricarica per continuare a giocare.")


root = tk.Tk()
root.title("Slot Machine")

credito = 20.0
costo_partita = 0.50

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0)

rullo1_label = ttk.Label(frame, text="", font=("Helvetica", 24))
rullo1_label.grid(row=0, column=0, padx=5, pady=5)

rullo2_label = ttk.Label(frame, text="", font=("Helvetica", 24))
rullo2_label.grid(row=0, column=1, padx=5, pady=5)

rullo3_label = ttk.Label(frame, text="", font=("Helvetica", 24))
rullo3_label.grid(row=0, column=2, padx=5, pady=5)

spin_button = ttk.Button(frame, text="Spin (Costo: {} euro)".format(costo_partita), command=spin)
spin_button.grid(row=1, columnspan=3, padx=5, pady=10)

risultato_label = ttk.Label(frame, text="Credito disponibile: {} euro".format(credito), font=("Helvetica", 16))
risultato_label.grid(row=2, columnspan=3, padx=5, pady=5)

root.mainloop()