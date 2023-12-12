import tkinter as tk
from tkinter import messagebox as mb
from Pessoa import Pessoa
from datetime import datetime as dt

#metodo limpar

def limpar() -> None:
    lista = [campName, campdate, campmes, campyear]
    
    for i in lista:
        i.delete(0,tk.END)

def getinputs():
    humano = Pessoa(campName.get(), dt(int(campyear.get()), int(campmes.get()), int(campdate.get())))
    limpar()
    mb.showinfo(title= "Dua idade é: ", message=humano)



#criar o frame principal

janela = tk.Tk()
janela.geometry("320x250")
janela.title("AgeCalc")

# Criar lables

nome = tk.Label(text= "Nome: ", height=2, font=("castellar", 14))
nome.grid(column= 0, row= 1)

dia = tk.Label(text= "Dia: ", height=2, font=("castellar", 14))
dia.grid(column= 0, row= 2)

mes = tk.Label(text= "Mês: ", height=2, font=("castellar", 14))
mes.grid(column= 0, row= 3)

ano = tk.Label(text= "Ano: ", height=2, font=("castellar", 14))
ano.grid(column= 0, row= 4)

#Criar campos (Fields)

campName = tk.Entry(width=12, font=("times new roman", 14))
campName.grid(column= 1, row= 1)

campdate = tk.Entry(font=("times new roman", 14))
campdate.grid(column= 1, row= 2)

campmes = tk.Entry(font=("times new roman", 14))
campmes.grid(column= 1, row= 3)

campyear = tk.Entry(font=("times new roman", 14))
campyear.grid(column= 1, row= 4)

# Criar bottoms

bcalc = tk.Button(janela, text="OK", width=10, font=("times new roman", 14))
bcalc.grid(column=1, row=5)

bClean = tk.Button(janela, text="LIMPAR", width=10, font=("times new roman", 14), command= limpar)
bClean.grid(column=0, row=5)

# Começar a GUI
janela.mainloop()
