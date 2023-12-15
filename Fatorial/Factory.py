from Factor import Factor
import tkinter as tk

def result():
    fator = Factor(int(campNum.get()))
    fatores = fator.fatorar()
    resultado["text"] = f"Resultado: {fatores}"

window = tk.Tk()
window.geometry("300x100")
window.title("Factorial Numbers")
window.anchor(anchor="center")

num = tk.Label(text="Digite um número para fatorar:", height= 1, font=("times new roman", 12, "bold"))
num.grid(column=0, row=0)

resultado = tk.Label(text="Resultado...", height=1, font=("times new roman", 11, "italic"))
resultado.grid(column=0, row=1)

campNum = tk.Entry(width=5, font=("times new roman", 12))
campNum.grid(column=1, row=0)

bFatores = tk.Button(window, text="Calcular", command=result, width=10, font=("times new roman", 12, "bold"))
bFatores.grid(column=0, row=2)


window.mainloop()