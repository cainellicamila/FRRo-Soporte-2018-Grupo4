''' Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los
nombre de Ciudades Argentinas y su código postal (por lo menos 5 ciudades).'''

import tkinter as tk
from tkinter import *
from tkinter import ttk

c= tk.Tk()

c.treeview = ttk.Treeview()
c.treeview.columnconfigure(0, weight=1)   # --- 1: tamaño modificable
c.treeview.rowconfigure(0, weight=1)      # --- 1: tamaño modificable

c.treeview.pack(fill=BOTH, expand=1,)
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

c.mainloop()
