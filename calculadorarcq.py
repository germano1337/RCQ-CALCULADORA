import tkinter as tk
from tkinter import messagebox

calculadora = tk.Tk()
calculadora.title("Calculadora RCQ")
calculadora.geometry("321x333")

def botaoCalcularClicado():
    if cintura.get() != "" and quadril.get() != "":
        c = float(cintura.get())
        q = float(quadril.get())
        rcq = c / q
        messagebox.showinfo("Resultado", "RCQ: " + str(rcq))

def botaoSairClicado():
    calculadora.quit()        
        
cintura = tk.StringVar()
quadril = tk.StringVar()

rotuloCintura = tk.Label(text="Cintura: ", width= 25 , anchor=tk.W)
textoCintura = tk.Entry(textvariable = cintura)
rotuloQuadril = tk.Label(text="Quadril: ", width= 25 , anchor=tk.W)
textoQuadril = tk.Entry(textvariable = quadril)

botaoCalcular = tk.Button(calculadora, text="Calcular", command=botaoCalcularClicado)
botaoSair = tk.Button(calculadora, text= "Sair", command= botaoSairClicado )


rotuloCintura.grid(row = 0, column =0)
textoCintura.grid(row = 0, column=1)
rotuloQuadril.grid(row = 1, column=0)    
textoQuadril.grid(row = 1, column=1)

botaoCalcular.grid(row = 2, column=0, columnspan=2)   
botaoSair.grid(row= 3, column = 0, columnspan= 3)



calculadora.mainloop()