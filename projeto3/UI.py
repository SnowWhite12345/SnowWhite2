import tkinter as tk

window = tk.Tk()
window.title("TK Example.py app")
window.geometry("400x300")
newlabel = tk.Label(text="Hello, world!")
newlabel.grid(column=1, row=3)
newlabel.pack(anchor="center")

window.mainloop()