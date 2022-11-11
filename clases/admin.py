from tkinter import messagebox
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

    # Se registra al medico en la base de datos
    def registrar_med(self, medico):
        pass

    # Se accede a la base de datos para modificar los datos del medico
    def modificar_med(self, medico):
        pass

    # Se accede a la base de datos para eliminar medico
    def eliminar_med(self, medico):
        pass

    # Se registra al enfermero en la base de datos
    def registrar_enf(self, enfermero):
        pass

    # Se accede a la base de datos para modificar los datos del enfermero
    def modificar_enf(self, enfermero):
        pass

    # Se accede a la base de datos para eliminar enfermero
    def eliminar_enf(self, enfermero):
        pass

    # Se registra pacientes en la base de datos
    def registrar_paciente(self, paciente):
        self.consulta = ("""INSERT INTO Paciente(dni, nombres, apellido_paterno, apellido_materno, telefono,
        fecha_nacimiento, direccion, sexo, email, observacion) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""")
        self.base_datos.cursor.execute(self.consulta, paciente.dni, paciente.nombres,
                                       paciente.apellido_paterno, paciente.apellido_materno, paciente.telefono,
                                       paciente.fecha_nacimiento,
                                       paciente.direccion, paciente.sexo, paciente.email, paciente.observacion)
        self.base_datos.cursor.commit()
        print('Paciente agregado.')

    def listar_datos_paciente(self):
        self.consulta = ('SELECT * FROM Paciente')
        self.base_datos.cursor.execute(self.consulta)
        self.datos_paciente = self.base_datos.cursor.fetchall()
        return self.datos_paciente

        # self.finalizar_conexion_db()

    # Se accede a la base de datos para modificar los datos de los pacientes
    def modificar_paciente(self, paciente, id_paciente):
        self.consulta = ("""UPDATE Paciente SET dni = ?, nombres = ?, apellido_paterno = ?,
        apellido_materno = ?, telefono = ?,
        fecha_nacimiento = ?, direccion = ?, sexo = ?, email = ?, observacion = ? WHERE id = ?""")
        self.base_datos.cursor.execute(self.consulta, paciente.dni, paciente.nombres,
                                       paciente.apellido_paterno, paciente.apellido_materno, paciente.telefono,
                                       paciente.fecha_nacimiento,
                                       paciente.direccion, paciente.sexo, paciente.email, paciente.observacion,
                                       id_paciente)
        self.base_datos.cursor.commit()
        print('Paciente modificado.')

    # Se accede a la base de datos para eliminar paciente
    def eliminar_paciente(self, id_paciente):
        self.consulta = ('DELETE FROM Paciente WHERE id = ?')
        self.base_datos.cursor.execute(self.consulta, id_paciente)
        self.base_datos.cursor.commit()
        print('Paciente eliminado.')
