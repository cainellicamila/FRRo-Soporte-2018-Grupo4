from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import tkinter as tk
from tkinter import *
from tkinter import ttk

from Datos.Datos01 import Socio, Base

from Negocio.Negocio01 import NegocioSocio, LongitudInvalida, DniRepetido, MaximoAlcanzado

def alta(s):
    d= tk.Tk()
    d.marco = ttk.Frame(d, borderwidth=4, relief="raised", padding=(10,10), style='My.TFrame')
    d.etq1 = ttk.Label(d.marco, text="Nombre:")
    d.etq2 = ttk.Label(d.marco, text="Apellido:")
    d.etq3 = ttk.Label(d.marco, text="DNI:")
    d.nombre= StringVar()
    d.apellido= StringVar()
    d.dni= StringVar()
    d.nombre = ttk.Entry(d.marco, textvariable= d.nombre, show="", width=30)
    d.apellido = ttk.Entry(d.marco, textvariable= d.apellido, show="", width=30)
    d.dni = ttk.Entry(d.marco, textvariable= d.dni, show="", width=30)
    d.aceptar=ttk.Button(d.marco, text="Aceptar", padding=(5,5), style="RB.TButton", command= lambda: aceptar(d,s))
    d.cancelar=ttk.Button(d.marco, text="Cancelar", padding=(5,5), style="RB.TButton", command= lambda: cancelar(d))

    d.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
    d.etq1.grid(column=0, row=0, sticky=(N, S, E, W), padx=5, pady=5)
    d.etq2.grid(column=0, row=1, sticky=(N, S, E, W), padx=5, pady=5)
    d.etq3.grid(column=0, row=2, sticky=(N, S, E, W), padx=5, pady=5)
    d.nombre.grid (column=1, row=0, sticky=(N, S, E, W), padx=5, pady=5)
    d.apellido.grid (column=1, row=1, sticky=(N, S, E, W), padx=5, pady=5)
    d.dni.grid (column=1, row=2, sticky=(N, S, E, W), padx=5, pady=5)
    d.aceptar.grid(column=0, row=3, padx=5, pady=5, sticky=(N, S, E, W))
    d.cancelar.grid(column=1, row=3, padx=5, pady=5, sticky=(N, S, E, W))


def baja(s):

    i=c.treeview.focus()
    j=c.treeview.item(i)
    k=j['values'][0]
    s.baja(k)
    c.treeview.delete(i)


def modificacion():

    d= tk.Tk()
    d.marco = ttk.Frame(d, borderwidth=4, relief="raised", padding=(10,10), style='My.TFrame')
    d.etq1 = ttk.Label(d.marco, text="Nombre:")
    d.etq2 = ttk.Label(d.marco, text="Apellido:")
    d.etq3 = ttk.Label(d.marco, text="DNI:")
    d.nombre= StringVar()
    d.apellido= StringVar()
    d.dni= StringVar()
    d.nombre = ttk.Entry(d.marco, textvariable= d.nombre, show="", width=30)
    d.apellido = ttk.Entry(d.marco, textvariable= d.apellido, show="", width=30)
    d.dni = ttk.Entry(d.marco, textvariable= d.dni, show="", width=30)
    d.aceptarMod=ttk.Button(d.marco, text="Aceptar", padding=(5,5), style="RB.TButton", command= lambda: aceptarMod(d,s))
    d.cancelar=ttk.Button(d.marco, text="Cancelar", padding=(5,5), style="RB.TButton", command= lambda: cancelar(d))

    d.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
    d.etq1.grid(column=0, row=0, sticky=(N, S, E, W), padx=5, pady=5)
    d.etq2.grid(column=0, row=1, sticky=(N, S, E, W), padx=5, pady=5)
    d.etq3.grid(column=0, row=2, sticky=(N, S, E, W), padx=5, pady=5)
    d.nombre.grid (column=1, row=0, sticky=(N, S, E, W), padx=5, pady=5)
    d.apellido.grid (column=1, row=1, sticky=(N, S, E, W), padx=5, pady=5)
    d.dni.grid (column=1, row=2, sticky=(N, S, E, W), padx=5, pady=5)
    d.aceptarMod.grid(column=0, row=3, padx=5, pady=5, sticky=(N, S, E, W))
    d.cancelar.grid(column=1, row=3, padx=5, pady=5, sticky=(N, S, E, W))

def aceptarMod (d,s):
    i=c.treeview.focus()
    j=c.treeview.item(i)
    k=j['values'][0]

    try:
        s.modificacion(Socio(id=str(k),nombre=str(d.nombre.get()),apellido=str(d.apellido.get()),dni=str(d.dni.get())))
        socio=s.buscar_dni(str(d.dni.get()))
        c.treeview.item(i, values=(socio.id, socio.nombre, socio.apellido, socio.dni) )
    except LongitudInvalida as e:
        print(e.args)
    except DniRepetido as e:
        print(e.args)
    except MaximoAlcanzado as e:
        print(e.args)

    d.destroy()

def aceptar (d,s):


    try:
        s.alta(Socio(nombre=str(d.nombre.get()),apellido=str(d.apellido.get()),dni=str(d.dni.get())))
        socio=s.buscar_dni(str(d.dni.get()))
        c.treeview.insert("", tk.END, values=(socio.id, socio.nombre, socio.apellido, socio.dni))
    except LongitudInvalida as e:
        print(e.args)
    except DniRepetido as e:
        print(e.args)
    except MaximoAlcanzado as e:
        print(e.args)

    d.destroy()

def cancelar (d):

    d.destroy()

c= tk.Tk()

c.marco = ttk.Frame(c, borderwidth=4, relief="raised", padding=(10,10), style='My.TFrame')
c.treeview = ttk.Treeview(c.marco)
c.treeview.columnconfigure(0, weight=1)   # --- 1: tamaño modificable
c.treeview.rowconfigure(0, weight=1)      # --- 1: tamaño modificable

c.title('ABM Socios')

c.treeview= ttk.Treeview(c.marco, column=("column1", "column2", "column3", "column4"), show='headings')
c.treeview.heading('column1', text='ID')
c.treeview.heading('column2', text='Nombre')
c.treeview.heading('column3', text='Apellido')
c.treeview.heading('column4', text='DNI')
c.treeview.pack()

s= NegocioSocio()
s.datos.borrar_todos()
s.alta(Socio(nombre='Camila', apellido='Cainelli', dni='40119128'))
s.alta(Socio(nombre='Hilda', apellido='Veron', dni='40555998'))

socios=s.todos()

for i in socios:
    c.treeview.insert("", tk.END, values=(i.id, i.nombre, i.apellido, i.dni))


c.treeview.pack(fill=BOTH, expand=1)
c.marco.pack(fill=BOTH, expand=1)

c.balta = ttk.Button(c.marco, text="Alta", padding=(5,5), style="RB.TButton", command= lambda: alta(s))
c.bbaja = ttk.Button(c.marco, text="Baja", padding=(5,5), style="RB.TButton", command= lambda: baja(s))
c.bmodif = ttk.Button(c.marco, text="Modificacion", padding=(5,5), style="RB.TButton", command= lambda: modificacion())
c.mensaje= ttk.Label(c.marco, text='Para realizar una alta presione el boton e ingrese los datos. Para una baja o modificacion selecione un socio y presione el boton correspondiente')
c.balta.pack(side=LEFT, fill=X, expand=1)
c.bbaja.pack(side=LEFT, fill=X, expand=1)
c.bmodif.pack(side=LEFT, fill=X, expand=1)

c.mensaje.pack(side=RIGHT,fill=X, expand=1)

c.mainloop()
