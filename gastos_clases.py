from cgitb import enable
from distutils.cmd import Command
from faulthandler import disable
from tkinter import *
from turtle import heading, title
from tkinter import ttk
import sys
from tkinter import messagebox
import sqlite3
import tkinter.font as font






conexion=sqlite3.connect("bd1.db")
try:
    conexion.execute("""create table gastos (
                              fecha text,
                              salida text,
                              tipo text,
                              vehiculo text,
                              proveedor text,
                              precio text
                    )""")

    print("se creo la tabla articulos")   

except sqlite3.OperationalError:

    print("La tabla articulos ya existe")     

conexion.close()



class Formulario_Gastos(Frame):

    def __init__(self, master=None):
        super().__init__(master,width="400", height="400")
        self.master = master
        self.pack()
        self.DibujarContenido()

        
        
    
    def DibujarContenido(self):
        self.opcion = IntVar()
        self.lblfecha = Label(self, text = "Fecha").place(x=5, y=5)
        self.mifecha = StringVar()
        self.entryfecha = Entry(self, textvariable = self.mifecha)
        self.entryfecha.place(x=80, y=5)
        self.misalida = StringVar()
        self.lblcomprobante = Label(self, text = "Salida").place(x=5, y=25)
        self.entrysalida = Entry(self, textvariable = self.misalida)
        self.entrysalida.place(x=80, y=25)
        self.lbltipodegasto = Label(self, text = "Tipo de Gasto").place(x=5, y=45)
        self.radiotipovehiculo = Radiobutton(self, text="Vehiculos", variable=self.opcion, value=1, command=lambda:[self.Mostrar(),self.Eleccion()])
        self.radiotipovehiculo.place(x=5, y=70)
        self.radiotipogenerales = Radiobutton(self, text="Generales", variable=self.opcion, value=2, command=lambda:[self.Mostrar(),self.Eleccion()])
        self.radiotipogenerales.place(x=5, y=90)
        self.radiotipopapeleria = Radiobutton(self, text="Papeleria", variable=self.opcion, value=3, command=lambda:[self.Mostrar(),self.Eleccion()])
        self.radiotipopapeleria.place(x=5, y=110)
        self.menudesplegable = ttk.Combobox(self, values=["LTO 318", "OCB 012", "ICP 627", "UFC 581", "VAZ 809", "FFC 291", "AB 154 UE", "WSH 915"], state="disabled")
        self.menudesplegable.place(x=5, y=140)
        self.miproveedor = StringVar()
        self.entryproveedor = Entry(self, textvariable = self.miproveedor)
        self.entryproveedor.place(x=5, y=170)
        self.miimporte = StringVar()
        self.entryimporte = Entry(self, textvariable = self.miimporte)
        self.entryimporte.place(x=5, y=190)
        self.btncargar = Button(self,text="Cargar", command=self.Validacion)
        self.btncargar.place(x=10, y=215)
        self.btnsalir = Button(self,text="Salir", command=self.Salir)
        self.btnsalir.place(x=60, y=215)
        self.eleccion = self.Eleccion()
        # self.consultar = Button(self.ventana, text="Consultar")
        # self.elecvehiculo = ""

    def Ocultar_Combo(self):
        self.menudesplegable.config(state="disabled")



    def Mostrar(self):
        if self.opcion.get()==1:
            self.menudesplegable.config(state="readonly")
        if self.opcion.get()!=1:
            self.menudesplegable.config(state="disabled")

    def Eleccion(self):
        if self.opcion.get()==1:
            self.eleccion = "Vehiculos"
        if self.opcion.get()==2:
            self.eleccion = "Generales"
        if self.opcion.get()==3:
            self.eleccion = "Papeleria"
            return self.eleccion

    def Guardar(self):
        conexion=sqlite3.connect("bd1.db")
        conexion.execute("insert into gastos values (:m_fecha, :m_salida, :m_opcion, :m_vehiculo, :m_proveedor, :m_importe)",
                    {
                        "m_fecha": self.mifecha.get(),
                        "m_salida": self.misalida.get(),
                        "m_opcion": self.eleccion,
                        "m_vehiculo": self.menudesplegable.get(),
                        "m_proveedor": self.miproveedor.get(),
                        "m_importe": self.miimporte.get()  
                    })
        conexion.commit()
        conexion.close()
    
    # def Eliminar(self):
    #      conexion=sqlite3.connect("bd1.db")
    
    def Reset(self):
        self.entryfecha.delete(0,END)
        self.entrysalida.delete(0,END)
        self.radiotipogenerales.deselect()
        self.radiotipovehiculo.deselect()
        self.radiotipopapeleria.deselect()
        self.menudesplegable.set("")
        self.entryproveedor.delete(0,END)
        self.entryimporte.delete(0,END)

    def Validacion(self):
        try:
            int(self.mifecha.get())
            str(self.misalida.get())
            str(self.miproveedor.get())
            float(self.miimporte.get())
        except:
            messagebox.showinfo(message="Tiene un error en algun campo")
        else:
            self.Guardar()
            self.Reset()
            self.Ocultar_Combo()




    def Salir(self):
        sys.exit()      








################!!PAGINA PRINCICPAL!!################

class Inicio(Frame):
    def __init__(self, master=None):
        super().__init__(master,width="700", height="700")
        self.master1 = master
        self.pack()
        self.Contenido_Inicial()

    def Contenido_Inicial(self):
        self.btnfont = font.Font(size=15, weight="bold")
        self.btncargar = Button(self,text="Cargar", bg="dark slate gray", fg="white", font=self.btnfont, command=self.Abrir_Carga)
        self.btncargar.place(x=165, y=130, width=105, height=38)
        self.btnconsultar = Button(self,text="Consultar", bg="dark slate gray", fg="white", font=self.btnfont)
        self.btnconsultar.place(x=165,y=190, width=105, height=38)

    def Abrir_Carga(self):
        aplicacion1.destroy()
        self.aplicacion = Formulario_Gastos(master=ventana)


        
ventana = Tk()
ventana.config(bg="blue")
ventana.title("APP GASTOS")
# aplicacion = Formulario_Gastos(master=ventana) 
aplicacion1 = Inicio(master=ventana) 
aplicacion1.config(width="400", height="400", bg="bisque")
ventana.mainloop()

