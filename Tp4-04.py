'''Ejercicio. Al Formulario del Ejercicio 3, agregue los siguientes botones:
1- un botón Alta que inicia otra ventana donde se pueda ingresar una ciudad y su
código postal
2 – un botón Baja que borra del listado de ciudades la ciudad que está seleccionada en
el Treeview .
3 – un botón Modificar. Todos los cambios se deben ver reflejados en la lista que se
muestra.'''


import tkinter as tk
from tkinter import *
from tkinter import ttk



def alta ():
    d= tk.Tk()
    d.marco = ttk.Frame(d, borderwidth=4, relief="raised", padding=(10,10), style='My.TFrame')
    d.cnueva= StringVar()
    d.cpnuevo= StringVar()
    d.etq1 = ttk.Label(d.marco, text="Ciudad:")
    d.etq2 = ttk.Label(d.marco, text="Codigo Postal:")
    d.cnueva = ttk.Entry(d.marco, textvariable= d.cnueva, show="", width=30)
    d.cpnuevo = ttk.Entry(d.marco, textvariable= d.cpnuevo, show="", width=30)
    d.ok=ttk.Button(d.marco, text="Ok", padding=(5,5), style="RB.TButton", command= lambda: ok(d))

    d.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
    d.etq1.grid(column=0, row=0, sticky=(N, S, E, W), padx=5, pady=5)
    d.etq2.grid(column=0, row=2, sticky=(N, S, E, W), padx=5, pady=5)
    d.cnueva.grid(column=0, row=1, padx=5, pady=5, sticky=(N, S, E, W))
    d.cpnuevo.grid(column=0, row=3, padx=5, pady=5, sticky=(N, S, E, W))
    d.ok.grid(column=0, row=4, padx=5, pady=5, sticky=(N, S, E, W))
    d.mainloop()

def borrar():
    i=c.treeview.focus()
    c.treeview.delete(i)

def edit ():
    i=c.treeview.focus()
    d= tk.Tk()
    d.marco = ttk.Frame(d, borderwidth=4, relief="raised", padding=(10,10), style='My.TFrame')
    d.etq1 = ttk.Label(d.marco, text="Nuevo campo")
    d.edicion= StringVar()
    d.edicion = ttk.Entry(d.marco, textvariable= d.edicion, show="", width=30)
    d.ok_2=ttk.Button(d.marco, text="Ok", padding=(5,5), style="RB.TButton", command= lambda: ok_2(d, i))

    d.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
    d.etq1.grid(column=0, row=0, sticky=(N, S, E, W), padx=5, pady=5)
    d.edicion.grid(column=0, row=1, padx=5, pady=5, sticky=(N, S, E, W))
    d.ok_2.grid(column=0, row=4, padx=5, pady=5, sticky=(N, S, E, W))
    print(i)

def ok (d):

    itemn=c.treeview.insert("", tk.END, text=d.cnueva.get())
    subitemn=c.treeview.insert(itemn, tk.END, text=d.cpnuevo.get())
    d.destroy()

def ok_2 (d, i):

    c.treeview.item(i, text=d.edicion.get())
    d.destroy()

c= tk.Tk()

c.marco = ttk.Frame(c, borderwidth=4, relief="raised", padding=(10,10), style='My.TFrame')
c.treeview = ttk.Treeview(c.marco)
c.treeview.columnconfigure(0, weight=1)   # --- 1: tamaño modificable
c.treeview.rowconfigure(0, weight=1)      # --- 1: tamaño modificable

c.title('Ciudades')


c.treeview.pack(fill=BOTH, expand=1)
item1 = c.treeview.insert("", tk.END, text="Rosario")
subitem1 = c.treeview.insert(item1, tk.END, text="2000")
item2 = c.treeview.insert("", tk.END, text="Santa Fe")
subitem2 = c.treeview.insert(item2, tk.END, text="3000")
item3 = c.treeview.insert("", tk.END, text="Cordoba")
subitem3 = c.treeview.insert(item3, tk.END, text="5000")
item4 = c.treeview.insert("", tk.END, text="Mendoza")
subitem4 = c.treeview.insert(item4, tk.END, text="5500")
item5 = c.treeview.insert("", tk.END, text="Parana")
subitem5 = c.treeview.insert(item5, tk.END, text="3100")

c.balta = ttk.Button(c.marco, text="Nueva ciudad", padding=(5,5), style="RB.TButton", command= lambda: alta())
c.bborar = ttk.Button(c.marco, text="Borrar ciudad", padding=(5,5), style="RB.TButton", command= lambda: borrar())
c.bedit = ttk.Button(c.marco, text="Editar", padding=(5,5), style="RB.TButton", command= lambda: edit())
c.balta.pack(fill=X, expand=1)
c.bborar.pack(fill=X, expand=1)
c.bedit.pack(fill=X, expand=1)

c.marco.pack(fill=BOTH, expand=1)


#estilos
style = ttk.Style()
style.configure("RB.TButton", background="white", font="bold")
c.config(bg="pink")

style.configure('My.TFrame', background='pink')

c.mainloop()

