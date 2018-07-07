import tkinter as tk
from tkinter import *
from tkinter import ttk

def sumar ():
        try:

                res= float(f1.ctext1.get())+float(f1.ctext2.get()) #toma el valor leido en el entry con el get,
                f1.resu.config(text='El resultado es:  '+ str(res)) # lo convertimos en float para sumarlo

        except (SyntaxError, NameError, TypeError, ZeroDivisionError):
                f1.resu.config(text='Error')

def restar ():
        try:
                res= float(f1.ctext1.get())-float(f1.ctext2.get())
                f1.resu.config(text='El resultado es:  '+ str(res))
        except (SyntaxError, NameError, TypeError, ZeroDivisionError):
                f1.resu.config(text='Error')

def dividir ():
        try:
                res= float(f1.ctext1.get())/float(f1.ctext2.get())
                f1.resu.config(text='El resultado es:  '+ str(res))
        except (SyntaxError, NameError, TypeError, ZeroDivisionError):
                f1.resu.config(text='Error')

def multiplicar ():
        try:
                res= float(f1.ctext1.get())*float(f1.ctext2.get())
                f1.resu.config(text='El resultado es:  '+ str(res)) #el + concatena
        except (SyntaxError, NameError, TypeError, ZeroDivisionError):
                f1.resu.config(text='Error')

f1 = tk.Tk()

f1.columnconfigure(0, weight=1)   # --- 1: tamaño modificable
f1.rowconfigure(0, weight=1)      # --- 1: tamaño modificable

f1.title("Calculadora")

f1.marco = ttk.Frame(f1, borderwidth=2, relief="raised", padding=(10,10))

f1.etq1 = ttk.Label(f1.marco, text="Primer operando:")
f1.etq2 = ttk.Label(f1.marco, text="Segundo operando:")

f1.num1=IntVar()
f1.num2=IntVar()

f1.ctext1 = ttk.Entry(f1.marco, textvariable=f1.num1, show="", width=30)
f1.ctext2 = ttk.Entry(f1.marco, textvariable=f1.num2, show="", width=30)

f1.boton1 = ttk.Button(f1.marco, text="+", padding=(5,5), command=lambda:sumar(), style="RB.TButton")
f1.boton2 = ttk.Button(f1.marco, text="-", padding=(5,5), command=lambda: restar(), style="RB.TButton")
f1.boton3 = ttk.Button(f1.marco, text="/", padding=(5,5), command=lambda: dividir(), style="RB.TButton")
f1.boton4 = ttk.Button(f1.marco, text="X", padding=(5,5), command=lambda: multiplicar(), style="RB.TButton")

f1.resu = ttk.Label(f1.marco, text="El resultado es:")

f1.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
f1.etq1.grid(column=0, row=0, sticky=(N, S, E, W), padx=5, pady=5)
f1.etq2.grid(column=1, row=0, sticky=(N, S, E, W), padx=5, pady=5)
f1.resu.grid(column=0, row=2, sticky=(N, S, E, W), columnspan=3, padx=5, pady=5)

f1.ctext1.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
f1.ctext2.grid(column=1, row=1, sticky=(E, W), padx=5, pady=5)
f1.boton1.grid(column=2, row=1, padx=5,sticky=(E,W,N,S))
f1.boton2.grid(column=3, row=1, padx=5,sticky=(W,E,N,S))
f1.boton3.grid(column=4, row=1, padx=5,sticky=(E,W,N,S))
f1.boton4.grid(column=5, row=1, padx=5,sticky=(W,E,N,S))

f1.marco.columnconfigure(0, weight=1)
f1.marco.columnconfigure(1, weight=1)
f1.marco.columnconfigure(2, weight=1)
f1.marco.columnconfigure(3, weight=1)
f1.marco.columnconfigure(4, weight=1)
f1.marco.columnconfigure(5, weight=1)
f1.marco.columnconfigure(0, weight=1)
f1.marco.rowconfigure(0, weight=1)
f1.marco.rowconfigure(1, weight=1)
f1.marco.rowconfigure(2, weight=1)

style = ttk.Style()
style.configure("RB.TButton", foreground="black", background="magenta")
f1.config(bg="pink")

f1.mainloop()


