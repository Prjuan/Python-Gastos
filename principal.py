from tkinter import *
import gastos_clases

class Principal:

    def __init__(self, master):
        self.ventana1 = master
        self.Dibujar()


    def Dibujar(self):
        self.btn_carga = Button(self.ventana1, text="CARGA DE GASTO")
        self.btn_carga.place(x=150, y=90, width=130, height=30)
        self.btn_consulta = Button(self.ventana1, text="CONSULTA")
        self.btn_consulta.place(x=150, y=170, width=130, height=30)

    # def Abrir_Carga(self):
    #     ventana1.withdraw()
        


# ventana1 = Tk()
# ventana1.title("APP GASTOS")
# ventana1.geometry("400x400")
# aplicacion = Principal(ventana1)
# ventana1.mainloop()