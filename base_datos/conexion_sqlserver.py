import pyodbc
import sys

class BD():
    contador_conexion = 0
    conexion = None
    cursor = None

    def iniciar_conexion_db(self):
        BD.contador_conexion += 1
        if BD.contador_conexion == 1:
            try:
                BD.conexion = pyodbc.connect('DRIVER={ODBC DRIVER 17 for SQL Server};SERVER=(local);DATABASE=Emssamlud;UID=lucas;PWD=123')
                print('Conexion exitosa')
            except Exception as ex:
                print(ex)
                # crear un box que muestra la alarma al usuario
                sys.exit("error en conexion a base de datos")

            BD.cursor = BD.conexion.cursor()
            print('Cursor creado')

    def finalizar_conexion_db(self):
        BD.cursor.close()
        print('Cursor cerrado')
        BD.conexion.close()
        print('Conexion finalizada')

