from cgitb import enable
from faulthandler import disable
from tkinter import *
from turtle import heading
from tkinter import ttk
import sys
from tkinter import messagebox
import sqlite3

conexion=sqlite3.connect("bd1.db")
try:
    conexion.execute("""create table gastos (
                              fecha text,
                              salida text,
                              tipo text,
                              proveedor text,
                              precio text
                    )""")

    print("se creo la tabla articulos")   

except sqlite3.OperationalError:

    print("La tabla articulos ya existe")     

conexion.close()



class Formulario_Gastos:

    def __init__(self, master):
        self.ventana = master
        self.DibujarContenido()

        
        
    
    def DibujarContenido(self):
        self.opcion = IntVar()
        self.lblfecha = Label(self.ventana , text = "Fecha").place(x=5, y=5)
        self.mifecha = StringVar()
        self.entryfecha = Entry(self.ventana, textvariable = self.mifecha)
        self.entryfecha.place(x=80, y=5)
        self.misalida = StringVar()
        self.lblcomprobante = Label(self.ventana , text = "Salida").place(x=5, y=25)
        self.entrysalida = Entry(self.ventana, textvariable = self.misalida)
        self.entrysalida.place(x=80, y=25)
        self.lbltipodegasto = Label(self.ventana , text = "Tipo de Gasto").place(x=5, y=45)
        self.radiotipovehiculo = Radiobutton(self.ventana, text="Vehiculos", variable=self.opcion, value=1, command=self.Mostrar)
        self.radiotipovehiculo.place(x=5, y=70)
        self.radiotipogenerales = Radiobutton(self.ventana, text="Generales", variable=self.opcion, value=2, command=self.Mostrar)
        self.radiotipogenerales.place(x=5, y=90)
        self.radiotipopapeleria = Radiobutton(self.ventana, text="Papeleria", variable=self.opcion, value=3, command=self.Mostrar)
        self.radiotipopapeleria.place(x=5, y=110)
        self.menudesplegable = ttk.Combobox(self.ventana, values=["LTO 318", "OCB 012", "ICP 627", "UFC 581", "VAZ 809", "FFC 291", "KTS 665", "WSH 915"], state="disabled")
        self.menudesplegable.place(x=5, y=140)
        self.miproveedor = StringVar()
        self.entryproveedor = Entry(self.ventana, textvariable = self.miproveedor)
        self.entryproveedor.place(x=5, y=170)
        self.miimporte = StringVar()
        self.entryimporte = Entry(self.ventana, textvariable = self.miimporte)
        self.entryimporte.place(x=5, y=190)
        self.btncargar = Button(self.ventana,text="Cargar", command=self.Guardar)
        self.btncargar.place(x=10, y=215)
        self.btnsalir = Button(self.ventana,text="Salir", command=self.Salir)
        self.btnsalir.place(x=60, y=215)
        
    def Mostrar(self):
        if self.opcion.get()==1:
            self.menudesplegable.config(state="readonly")
        if self.opcion.get()!=1:
            self.menudesplegable.config(state="disabled")

    # def Abrir(self):
    #     miConexion=sqlite3.connect("datagastos.db")
    #     miCursor=miConexion.cursor()

    #     datos=self.mifecha.get(), self.misalida.get(), self.opcion.get(), self.miproveedor.get(), self.miimporte.get()
        
    #     miCursor.execute("INSERT INTO GASTOS")

    def Guardar(self):
        # datos = (self.mifecha.get(), self.misalida.get(), self.opcion.get(), self.miproveedor.get(), self.miimporte.get())
        # con = sqlite3.connect("bd1.db")
        # cursor = con.cursor()
        # sql = "insert into GASTOS (fecha, salida, tipo, vehiculo, proveedor, importe) values(?, ?, ?, ?, ?, ?)"
        # cursor.execute(sql, datos)
        # con.commit()
        # con.close()
        conexion=sqlite3.connect("bd1.db")
        conexion.execute("insert into gastos values (:m_fecha, :m_salida, :m_opcion, :m_proveedor, :m_importe)",
                    {
                        "m_fecha": self.mifecha.get(),
                        "m_salida": self.misalida.get(),
                        "m_opcion": self.text.get(),
                        "m_proveedor": self.miproveedor.get(),
                        "m_importe": self.miimporte.get()  
                    })

        conexion.commit()
        conexion.close()
    
    

    def Salir(self):
        sys.exit()      


  






        
                







ventana = Tk()
ventana.title("CARGA DE GASTOS")
ventana.geometry("400x400")
aplicacion = Formulario_Gastos(ventana)
ventana.mainloop()