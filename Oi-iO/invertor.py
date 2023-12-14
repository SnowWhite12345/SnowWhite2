import tkinter as tk
from diálogo import Inverso
from tkinter import messagebox as mb

def limpar():
    lista = [campFrase]

    for input in lista:
        input.delete(0, tk.END)

def result():
    esarf = Inverso(campFrase.get())
    limpar()
    mb.showinfo(title="Resultado:", message=f"{esarf.inverter()}")


window = tk.Tk()
window.geometry("280x130")
window.title("Invert words")
window.anchor("center")
window.resizable(False, False)


frase = tk.Label(text = "Digite uma frase:", height = 2, font = ("times new roman", 13, "bold"))
frase.grid(column = 0, row = 0)

campFrase = tk.Entry(width=15, font=("times new roman", 12))
campFrase.grid(column=1, row=0)

bInvert = tk.Button(window, text="Ok!", command=result, width=10, font=("times new roman", 13, "bold"))
bInvert.grid(column= 1, row= 1)


bLimpar = tk.Button(window, text = "Limpar", command = limpar, width = 10, font = ("times new roman", 13, "bold"))
bLimpar.grid(column = 0, row = 1)

window.mainloop()