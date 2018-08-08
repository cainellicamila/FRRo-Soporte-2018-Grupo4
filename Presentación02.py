import tkinter as tk
from tkinter import *
from tkinter import ttk

from Datos.Datos01 import Socio, Base

from Negocio.Negocio01 import NegocioSocio, LongitudInvalida, DniRepetido, MaximoAlcanzado


class ABMForm:

    def __init__(self, parent, cn_socio):
        self.parent = parent
        self.cn_socio = cn_socio

        columns = ('ID', 'Nombre', 'Apellido', 'DNI')
        self.tree = ttk.Treeview(parent, columns=columns, show='headings')
        self.balta = Button(parent, text="Alta", command=lambda:self.altaSocio())
        self.bbaja = Button(parent, text="Baja", command=lambda:self.bajaSocio())
        self.bmodif = Button(parent, text="Modificacion", command=lambda:self.modificacion())


        self.tree.pack(fill=BOTH, expand=1)
        self.balta.pack(side=LEFT, fill=X, expand=1)
        self.bbaja.pack(side=LEFT, fill=X, expand=1)
        self.bmodif.pack(side=LEFT, fill=X, expand=1)

        self.refresh()

    def refresh(self):
        [self.tree.delete(c) for c in self.tree.get_children()]
        socios = self.cn_socio.todos()
        for s in socios:
            self.tree.insert('', 'end', text=s.id, values=(s.id, s.nombre, s.apellido, s.dni))

    def altaSocio(self):
        AltaModiForm(parent, self.refresh, self.cn_socio)
        self.refresh()

    def bajaSocio(self):
        i = self.tree.focus()
        j = self.tree.item(i)
        k = j['values'][0]
        self.cn_socio.baja(k)
        self.tree.delete(i)
        self.refresh()

    def modificacion(self):
        item = self.tree.selection()[0]
        id_socio = self.tree.item(item, 'values')[0]
        AltaModiForm(self.parent, self.refresh, self.cn_socio, self.cn_socio.buscar(id_socio))
        self.refresh()


class AltaModiForm:

    def __init__(self, parent, callback, cn_socio, socio=None):
        self.callback = callback
        self.cn_socio = cn_socio

        self.form =Toplevel()
        self.form.title('Alta/Modificacion')
        self.form.transient(master=parent)


        label_nombre = Label(self.form, text='Nombre', width=10)
        label_apellido = Label(self.form, text='Apellido', width=10)
        label_dni = Label(self.form, text='DNI', width=10)

        self.var_id = IntVar(value=getattr(socio, 'id', 0))
        self.var_nombre = StringVar(value=getattr(socio, 'nombre', ''))
        self.var_apellido = StringVar(value=getattr(socio, 'apellido', ''))
        self.var_dni = IntVar(value=getattr(socio, 'dni', 0))


        input_nombre = Entry(self.form, textvariable=self.var_nombre)
        input_apellido = Entry(self.form, textvariable=self.var_apellido)
        input_dni = Entry(self.form, textvariable=self.var_dni)

        # botones
        aceptar = Button(self.form, text='Aceptar', command=self.aceptar)
        cancelar = Button(self.form, text='Cancelar', command=self.cerrar)
        # seteamos la accion que corresponde
        self.accion = self.modif if socio else self.alta


        label_nombre.grid(row=0, column=0)
        label_apellido.grid(row=1, column=0)
        label_dni.grid(row=2, column=0)

        input_nombre.grid(row=0, column=1)
        input_apellido.grid(row=1, column=1)
        input_dni.grid(row=2, column=1)

        aceptar.grid(row=3, column=0)
        cancelar.grid(row=3, column=1)



    def aceptar(self):
        self.accion()
        self.callback
        self.cerrar()


    def cerrar(self):
        self.form.destroy()

    def alta(self):
        self.cn_socio.alta(Socio(nombre=self.var_nombre.get(), apellido=self.var_apellido.get(), dni=self.var_dni.get()))

    def modif(self):
        self.cn_socio.modificacion(Socio(id=self.var_id.get(), nombre= self.var_nombre.get(),apellido= self.var_apellido.get(),dni= self.var_dni.get()))



parent = tk.Tk()
parent.title("ABM Socios")
parent.marco = ttk.Frame(parent, borderwidth=1, relief="raised", padding=(10, 10))

parent.marco.pack(fill=BOTH, expand=1)
cn_socio = NegocioSocio()

ABMForm(parent.marco, cn_socio)

parent.mainloop()
