# DAO: Data Access Object

class DAOPaciente(DAO):
    def insertar_paciente(self, paciente):
        query = ("""INSERT INTO Paciente(dni, nombres, apellido_paterno, apellido_materno, telefono,
            fecha_nacimiento, direccion, sexo, email, observacion) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""")
        self._cursor.execute(query, 
                paciente.dni, 
                paciente.nombres,
                paciente.apellido_paterno, 
                paciente.apellido_materno, 
                paciente.telefono, 
                paciente.fecha_nacimiento,
                paciente.direccion, 
                paciente.sexo, 
                paciente.email, 
                paciente.observacion)
        self._cursor.commit()
        print('Paciente agregado.')
