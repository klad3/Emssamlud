from tkinter import messagebox
from tkinter import *
import base_datos.conexion_sqlserver as bd

class Admin():
    def __init__(self):
        self.__usuario = 'Admin'
        self.__password = '123'
        self.base_datos = bd.BD()
        self.base_datos.iniciar_conexion_db()

    def finalizar_conexion_db(self):
        self.base_datos.finalizar_conexion_db()

    def login(self, usuario, password):
        self.accede_sistema = False
        if usuario == self.__usuario and password == self.__password:
            self.accede_sistema = True
        else:
            messagebox.showwarning('Advertencia', 'Usuario y/o contraseña incorrectos')

    def listar_datos_medico(self):
        self.consulta = ('SELECT * FROM Medico')
        self.base_datos.cursor.execute(self.consulta)
        self.datos_medicos = self.base_datos.cursor.fetchall()
        return self.datos_medicos

    def listar_datos_enfermero(self):
        self.consulta = ('SELECT * FROM Enfermero')
        self.base_datos.cursor.execute(self.consulta)
        self.datos_enfermeros = self.base_datos.cursor.fetchall()
        return self.datos_enfermeros

    def registrar_med(self, medico):
        self.consulta = ("""INSERT INTO Medico(dni, nombres, apellido_paterno, apellido_materno,
        telefono, ocupacion, sexo, disponibilidad, especialidad) values(?, ?, ?, ?, ?, ?, ?, ?, ?)""")
        self.base_datos.cursor.execute(self.consulta, medico._dni, medico._nombres,
        medico._apellido_paterno, medico._apellido_materno, medico._telefono, medico._ocupacion,
        medico._sexo, medico._disponibilidad, medico.especialidad)
        self.base_datos.cursor.commit()
        print('Médico registrado.')

    def modificar_med(self, medico, id_medico):
        self.consulta = ("""UPDATE Medico SET dni = ?, nombres = ?, apellido_paterno = ?,
        apellido_materno = ?, telefono = ?,
        ocupacion = ?, sexo = ?, disponibilidad = ?, especialidad = ? WHERE id = ?""")
        self.base_datos.cursor.execute(self.consulta, medico._dni, medico._nombres,
        medico._apellido_paterno, medico._apellido_materno, medico._telefono,  medico._ocupacion,
        medico._sexo, medico._disponibilidad, medico.especialidad, id_medico)
        self.base_datos.cursor.commit()
        print('Médico modificado.')
    
    def eliminar_med(self, id_medico):
        self.consulta = ('DELETE FROM Medico WHERE id = ?')
        self.base_datos.cursor.execute(self.consulta, id_medico)
        self.base_datos.cursor.commit()
        print('Médico eliminado.')

    def registrar_enf(self, enfermero):
        self.consulta = ("""INSERT INTO Enfermero(dni, nombres, apellido_paterno, apellido_materno,
        telefono, ocupacion, sexo, disponibilidad, area) values(?, ?, ?, ?, ?, ?, ?, ?, ?)""")
        self.base_datos.cursor.execute(self.consulta, enfermero._dni, enfermero._nombres,
        enfermero._apellido_paterno, enfermero._apellido_materno, enfermero._telefono, enfermero._ocupacion,
        enfermero._sexo, enfermero._disponibilidad, enfermero.area)
        self.base_datos.cursor.commit()
        print('Enfermero registrado.')
    
    def modificar_enf(self, enfermero, id_enfermero):
        self.consulta = ("""UPDATE Enfermero SET dni = ?, nombres = ?, apellido_paterno = ?,
        apellido_materno = ?, telefono = ?,
        ocupacion = ?, sexo = ?, disponibilidad = ?, area = ? WHERE id = ?""")
        self.base_datos.cursor.execute(self.consulta, enfermero._dni, enfermero._nombres,
        enfermero._apellido_paterno, enfermero._apellido_materno, enfermero._telefono,  enfermero._ocupacion,
        enfermero._sexo, enfermero._disponibilidad, enfermero.area, id_enfermero)
        self.base_datos.cursor.commit()
        print('Enfermero modificado.')

    def eliminar_enf(self, id_enfermero):
        self.consulta = ('DELETE FROM Enfermero WHERE id = ?')
        self.base_datos.cursor.execute(self.consulta, id_enfermero)
        self.base_datos.cursor.commit()
        print('Enfermero eliminado.')

    def listar_datos_paciente(self):
        self.consulta = ('SELECT * FROM Paciente')
        self.base_datos.cursor.execute(self.consulta)
        self.datos_paciente = self.base_datos.cursor.fetchall()
        return self.datos_paciente

    def registrar_paciente(self, paciente):
        self.consulta = ("""INSERT INTO Paciente(dni, nombres, apellido_paterno, apellido_materno, telefono,
        fecha_nacimiento, direccion, sexo, email, observacion) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""")
        self.base_datos.cursor.execute(self.consulta, paciente.dni, paciente.nombres,
        paciente.apellido_paterno, paciente.apellido_materno, paciente.telefono, paciente.fecha_nacimiento,
        paciente.direccion, paciente.sexo, paciente.email, paciente.observacion)
        self.base_datos.cursor.commit()
        print('Paciente agregado.')
    
    def modificar_paciente(self, paciente, id_paciente): 
        self.consulta = ("""UPDATE Paciente SET dni = ?, nombres = ?, apellido_paterno = ?,
        apellido_materno = ?, telefono = ?,
        fecha_nacimiento = ?, direccion = ?, sexo = ?, email = ?, observacion = ? WHERE id = ?""")
        self.base_datos.cursor.execute(self.consulta, paciente.dni, paciente.nombres,
        paciente.apellido_paterno, paciente.apellido_materno, paciente.telefono,  paciente.fecha_nacimiento,
        paciente.direccion, paciente.sexo, paciente.email, paciente.observacion, id_paciente)
        self.base_datos.cursor.commit()
        print('Paciente modificado.')

    def eliminar_paciente(self, id_paciente):
        self.consulta = ('DELETE FROM Paciente WHERE id = ?')
        self.base_datos.cursor.execute(self.consulta, id_paciente)
        self.base_datos.cursor.commit()
        print('Paciente eliminado.')