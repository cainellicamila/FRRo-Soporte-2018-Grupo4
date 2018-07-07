import tkinter as tk
from tkinter import *
from tkinter import ttk

#funcion que toma el numero del boton y lo concatena

def click (num):
    c.cuenta.set(c.entrada.get()+ str(num))

#evalua el string formado por la concatenacion de botones apretados y devuelve el resultado
def igual():
    try:
        resultado =eval(c.cuenta.get())
        c.cuenta.set(str(resultado))

    except (SyntaxError, NameError, TypeError, ZeroDivisionError):
        c.cuenta.set('Error')
#limpia la variable cuenta para poder calcular otro resultado
def clear():
    c.cuenta.set(str())

c = tk.Tk()
c.cuenta = StringVar()
c.columnconfigure(0, weight=1)   # --- 1: tamaño modificable
c.rowconfigure(0, weight=1)      # --- 1: tamaño modificable

c.title("Calculadora")

c.marco = ttk.Frame(c, borderwidth=4, relief="raised", padding=(10,10))

#declaracion de la unica entrada. No se como mandarle lo de los botones ni que lo vaya mostrando
c.entrada = ttk.Entry(c.marco, width=30, textvariable=c.cuenta, show="")

#declaracion de botones
c.b1 = ttk.Button(c.marco, text="1", padding=(5,5), style="RB.TButton", command= lambda: click('1'))
c.b2 = ttk.Button(c.marco, text="2", padding=(5,5), style="RB.TButton", command= lambda: click('2'))
c.b3 = ttk.Button(c.marco, text="3", padding=(5,5), style="RB.TButton", command= lambda: click('3'))
c.b4 = ttk.Button(c.marco, text="4", padding=(5,5), style="RB.TButton", command= lambda: click('4'))
c.b5 = ttk.Button(c.marco, text="5", padding=(5,5), style="RB.TButton", command= lambda: click('5'))
c.b6 = ttk.Button(c.marco, text="6", padding=(5,5), style="RB.TButton", command= lambda: click('6'))
c.b7 = ttk.Button(c.marco, text="7", padding=(5,5), style="RB.TButton", command= lambda: click('7'))
c.b8 = ttk.Button(c.marco, text="8", padding=(5,5), style="RB.TButton", command= lambda: click('8'))
c.b9 = ttk.Button(c.marco, text="9", padding=(5,5), style="RB.TButton", command= lambda: click('9'))
c.bsum = ttk.Button(c.marco, text="+", padding=(5,5), style="RB.TButton", command= lambda: click('+'))
c.bres = ttk.Button(c.marco, text="-", padding=(5,5), style="RB.TButton", command= lambda: click('-'))
c.bdiv = ttk.Button(c.marco, text="/", padding=(5,5), style="RB.TButton", command= lambda: click('/'))
c.bmul = ttk.Button(c.marco, text="X", padding=(5,5), style="RB.TButton", command= lambda: click('*'))
c.bi = ttk.Button(c.marco, text="=", padding=(5,5), style="RB.TButton", command= lambda: igual())
c.b0 = ttk.Button(c.marco, text="0", padding=(5,5), style="RB.TButton", command= lambda: click('0'))
c.bc = ttk.Button(c.marco, text="C", padding=(5,5), style="RB.TButton", command= lambda: clear())

#configuracion de la ubicacion de las cosas en el marco
c.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
c.entrada.grid(column=0, row=0, sticky=(E, W), padx=5, pady=5, columnspan=4)
c.b7.grid(column=0, row=1, padx=5, pady=5,sticky=(E,W,N,S))
c.b8.grid(column=1, row=1, padx=5, pady=5,sticky=(E,W,N,S))
c.b9.grid(column=2, row=1, padx=5, pady=5,sticky=(E,W,N,S))
c.bsum.grid(column=3, row=1, padx=5, pady=5,sticky=(E,W,N,S))
c.b4.grid(column=0, row=2, padx=5, pady=5,sticky=(E,W,N,S))
c.b5.grid(column=1, row=2, padx=5, pady=5,sticky=(E,W,N,S))
c.b6.grid(column=2, row=2, padx=5, pady=5,sticky=(E,W,N,S))
c.bres.grid(column=3, row=2, padx=5, pady=5,sticky=(E,W,N,S))
c.b1.grid(column=0, row=3, padx=5, pady=5,sticky=(E,W,N,S))
c.b2.grid(column=1, row=3, padx=5, pady=5,sticky=(E,W,N,S))
c.b3.grid(column=2, row=3, padx=5, pady=5,sticky=(E,W,N,S))
c.bdiv.grid(column=3, row=3, padx=5, pady=5,sticky=(E,W,N,S))
c.b0.grid(column=0, row=4, padx=5, pady=5,sticky=(E,W,N,S))
c.bi.grid(column=1, row=4, padx=5, pady=5,sticky=(E,W,N,S))
c.bmul.grid(column=3, row=4, padx=5, pady=5,sticky=(E,W,N,S))
c.bc.grid(column=2, row=4, padx=5, pady=5,sticky=(E,W,N,S))

#Para que se expandan los botones y la entrada

c.marco.columnconfigure(0, weight=1)
c.marco.columnconfigure(1, weight=1)
c.marco.columnconfigure(2, weight=1)
c.marco.columnconfigure(3, weight=1)
c.marco.rowconfigure(0, weight=1)
c.marco.rowconfigure(1, weight=1)
c.marco.rowconfigure(2, weight=1)
c.marco.rowconfigure(3, weight=1)
c.marco.rowconfigure(4, weight=1)




#estilos
style = ttk.Style()
style.configure("RB.TButton", background="magenta", font="bold")
c.config(bg="grey")

c.mainloop()
