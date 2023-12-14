#from Factor import Factor
import tkinter as tk

window = tk.Tk()
window.geometry("280x100")
window.title("Fatorial Numbers")

num = tk.Label(text="Digite um número para fatorar:", height= 4, font=("times new roman", 12, "bold"))
num.grid(column=0, row=0)


window.mainloop()