# import sqlite3


# class Gastos():

#     def Agregar(self):
#         datos = (self.mifecha.get(), self.misalida.get(), self.opcion.get(), self.miproveedor.get(), self.miimporte.get())
#         self.gastos1.Alta(datos)
        
#         self.descripcioncarga.set("")
#         self.preciocarga.set("")
    
#     def Abrir(self):
#         miConexion=sqlite3.connect("./datagastos.db")
#         return miConexion

#     def Alta(self, datos):
#         con = self.Abrir()
#         cursor = con.cursor()
#         sql = "insert into GASTOS (fecha, salida, tipo de gasto, vehiculo, proveedor, importe) values(?, ?, ?, ?, ?, ?)"
#         cursor.execute(sql, datos)
#         con.commit()
#         con.close()







