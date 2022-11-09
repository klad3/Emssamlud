from tkinter import *
import tkinter.ttk as ttk
import util.centrar_ventana as utl

class MenuEmssamlud(Toplevel):
    contador_frame_inicio = 0
    contador_frame_paciente = 0
    contador_frame_personal_salud = 0
    contador_frame_agendar_cita = 0
    def __init__(self):
        super().__init__()
        self.geometry('1200x600')
        utl.centrar_ventana(self, 1200, 600)
        self.title('Emsamlud - Sistema')
        self.config(bg='#0EB06E')
        self.resizable(False, False)
        self.disenno_interfaz_menu_principal()
        self.menu_opciones()

    def crear_frame_paciente(self):
        self.frame_opciones_inicio.destroy()
        MenuEmssamlud.contador_frame_paciente += 1
        
        self.frame_registro_pacientes = Frame(self.ventana_principal)
        self.frame_registro_pacientes.config(bg='#0EB06E', padx=10, pady=20)
        self.frame_registro_pacientes.grid(row=0, column=3, rowspan=6)

        self.label_dni_paciente = Label(self.frame_registro_pacientes, text='DNI', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_dni_paciente.grid(row=0, column=0, padx=(40, 20), sticky=W)
        self.label_nombres_paciente = Label(self.frame_registro_pacientes, text='Nombres', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_nombres_paciente.grid(row=1, column=0, padx=(40, 20), sticky=W)
        self.label_apellido_paterno_paciente = Label(self.frame_registro_pacientes, text='Apellido paterno', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_apellido_paterno_paciente.grid(row=2, column=0, padx=(40, 20), sticky=W)
        self.label_apellido_materno_paciente = Label(self.frame_registro_pacientes, text='Apellido materno', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_apellido_materno_paciente.grid(row=3, column=0, padx=(40, 20), sticky=W)
        self.label_telefono_paciente = Label(self.frame_registro_pacientes, text='Teléfono', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_telefono_paciente.grid(row=4, column=0, padx=(40, 0), sticky=W)

        self.label_fecha_nacimiento_paciente = Label(self.frame_registro_pacientes, text='Fecha de nacimiento', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_fecha_nacimiento_paciente.grid(row=0, column=2, padx=(100, 20), sticky=W)
        self.label_direccion_paciente = Label(self.frame_registro_pacientes, text='Direccion', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_direccion_paciente.grid(row=1, column=2, padx=(100, 20), sticky=W)
        self.label_sexo_paciente = Label(self.frame_registro_pacientes, text='Sexo', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_sexo_paciente.grid(row=2, column=2, padx=(100, 20), sticky=W)
        self.label_email_paciente = Label(self.frame_registro_pacientes, text='Email', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_email_paciente.grid(row=3, column=2, padx=(100, 20), sticky=W)
        self.label_observacion = Label(self.frame_registro_pacientes, text='Observación', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_observacion.grid(row=4, column=2, padx=(100, 20), sticky=W)
        
        self.cuadro_dni_paciente = Entry(self.frame_registro_pacientes, text='DNI', font=('Times New Roman', 10, 'bold'))
        self.cuadro_dni_paciente.grid(row=0, column=1)
        self.cuadro_nombres_paciente = Entry(self.frame_registro_pacientes, font=('Times New Roman', 10, 'bold'))
        self.cuadro_nombres_paciente.grid(row=1, column=1)
        self.cuadro_apellido_paterno_paciente = Entry(self.frame_registro_pacientes, font=('Times New Roman', 10, 'bold'))
        self.cuadro_apellido_paterno_paciente.grid(row=2, column=1)
        self.cuadro_apellido_materno_paciente = Entry(self.frame_registro_pacientes, font=('Times New Roman', 10, 'bold'))
        self.cuadro_apellido_materno_paciente.grid(row=3, column=1)
        self.cuadro_telefono_paciente = Entry(self.frame_registro_pacientes, font=('Times New Roman', 10, 'bold'))
        self.cuadro_telefono_paciente.grid(row=4, column=1)

        self.cuadro_fecha_nacimiento_paciente = Entry(self.frame_registro_pacientes, font=('Times New Roman', 10, 'bold'))
        self.cuadro_fecha_nacimiento_paciente.grid(row=0, column=3, padx=(20, 0), sticky=W)
        
        self.cuadro_direccion_paciente = Entry(self.frame_registro_pacientes, font=('Times New Roman', 10, 'bold'), width=25)
        self.cuadro_direccion_paciente.grid(row=1, column=3, padx=(20, 0), sticky=W)
        self.opciones_sexo_paciente = ttk.Combobox(self.frame_registro_pacientes, state='readonly', values=['Masculino', 'Femenino'], font=('Times New Roman', 10, 'bold'), width=23)
        self.opciones_sexo_paciente.set('Seleccione su sexo')
        self.opciones_sexo_paciente.grid(row=2, column=3, padx=(20, 0), sticky=W)
        self.cuadro_email_paciente = Entry(self.frame_registro_pacientes, font=('Times New Roman', 10, 'bold'), width=25)
        self.cuadro_email_paciente.grid(row=3, column=3, padx=(20, 0), sticky=W)

        self.frame_obs = Frame(self.frame_registro_pacientes, bg='#0EB06E', height=100)
        self.frame_obs.grid(row=4, column=3, padx=(20, 0), sticky=W, columnspan=2)

        self.cuadro_obs = Text(self.frame_obs, font=('Times New Roman', 10, 'bold'), width=25, height=3.5)
        self.cuadro_obs.grid(row=0, column=0, sticky=W)
        
        self.scroll_cuadro_obs = Scrollbar(self.frame_obs, command=self.cuadro_obs.yview)
        self.scroll_cuadro_obs.grid(row=0, column=1, sticky=NS, padx=10)
        self.cuadro_obs.config(yscrollcommand=self.scroll_cuadro_obs.set)

        self.frame_opciones_registro_pacientes = Frame(self.frame_registro_pacientes)
        self.frame_opciones_registro_pacientes.config(bg='#0EB06E', pady=20)
        self.frame_opciones_registro_pacientes.grid(row=5, column=0, columnspan=5, ipadx=50)

        self.opcion_limpiar_campos = Button(self.frame_opciones_registro_pacientes, text='Limpiar', cursor='hand2')
        self.opcion_limpiar_campos.grid(row=0, column=0, padx=70)

        self.opcion_registrar_paciente = Button(self.frame_opciones_registro_pacientes, text='Registrar', cursor='hand2')
        self.opcion_registrar_paciente.grid(row=0, column=1, padx=70)

        self.opcion_modificar_paciente = Button(self.frame_opciones_registro_pacientes, text='Modificar', cursor='hand2')
        self.opcion_modificar_paciente.grid(row=0, column=2, padx=70)

        self.opcion_eliminar_paciente = Button(self.frame_opciones_registro_pacientes, text='Eliminar', cursor='hand2')
        self.opcion_eliminar_paciente.grid(row=0, column=3, padx=70)

        def tabla_pacientes():
            tabla_pacientes = ttk.Treeview(self.frame_registro_pacientes, columns=('DNI', 'Nombres',
            'Apellido paterno', 'Apellido materno', 'Teléfono', 'Fecha de nacimiento',
            'Dirección', 'Sexo','Email', 'Observación'), height=3)   

            tabla_pacientes.column('#0', width=50, anchor=W)
            tabla_pacientes.column('DNI', width=60, anchor=CENTER)
            tabla_pacientes.column('Nombres', width=80, anchor=CENTER)
            tabla_pacientes.column('Apellido paterno', width=80, anchor=CENTER)
            tabla_pacientes.column('Apellido materno', width=80, anchor=CENTER)
            tabla_pacientes.column('Teléfono', width=60, anchor=CENTER)
            tabla_pacientes.column('Fecha de nacimiento', width=120, anchor=CENTER)
            tabla_pacientes.column('Dirección', width=60, anchor=CENTER)
            tabla_pacientes.column('Sexo', width=40, anchor=CENTER)
            tabla_pacientes.column('Email', width=50, anchor=CENTER)
            tabla_pacientes.column('Observación', width=100, anchor=CENTER)
            tabla_pacientes.config(padding=(3, 10))
            tabla_pacientes.grid(row=6, column=0, columnspan=4, padx=(40, 0))

            tabla_pacientes.heading('#0', text='ID')
            tabla_pacientes.heading('#1', text='DNI')
            tabla_pacientes.heading('#2', text='Nombres')
            tabla_pacientes.heading('#3', text='Apellido paterno')
            tabla_pacientes.heading('#4', text='Apellido materno')
            tabla_pacientes.heading('#5', text='Teléfono')
            tabla_pacientes.heading('#6', text='Fecha de nacimiento')
            tabla_pacientes.heading('#7', text='Dirección')
            tabla_pacientes.heading('#8', text='Sexo')
            tabla_pacientes.heading('#9', text='Email')
            tabla_pacientes.heading('#10', text='Observación')

            scroll_vertical_tabla_pacientes = Scrollbar(self.frame_registro_pacientes, command=tabla_pacientes.yview)
            scroll_vertical_tabla_pacientes.grid(row=6, column=4, sticky=NS, padx=(0, 10))
            tabla_pacientes.configure(yscrollcommand=scroll_vertical_tabla_pacientes.set)

        tabla_pacientes()

    def crear_frame_registro_personal_salud(self):
        self.contador_abrir_calendario = 0
        MenuEmssamlud.contador_frame_personal_salud += 1
        self.frame_opciones_inicio.destroy()
        self.frame_registro_personal_salud = Frame(self.ventana_principal)
        self.frame_registro_personal_salud.config(bg='#0EB06E', padx=10, pady=20)
        self.frame_registro_personal_salud.grid(row=0, column=3, rowspan=6)

        self.label_dni_personal_salud = Label(self.frame_registro_personal_salud, text='DNI', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_dni_personal_salud.grid(row=0, column=0, padx=(40, 20), sticky=W)
        self.label_nombres_personal_salud = Label(self.frame_registro_personal_salud, text='Nombres', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_nombres_personal_salud.grid(row=1, column=0, padx=(40, 20), sticky=W)
        self.label_apellido_paterno_personal_salud = Label(self.frame_registro_personal_salud, text='Apellido paterno', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_apellido_paterno_personal_salud.grid(row=2, column=0, padx=(40, 20), sticky=W)
        self.label_apellido_materno_personal_salud = Label(self.frame_registro_personal_salud, text='Apellido materno', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_apellido_materno_personal_salud.grid(row=3, column=0, padx=(40, 20), sticky=W)
        self.label_telefono_personal_salud = Label(self.frame_registro_personal_salud, text='Teléfono', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_telefono_personal_salud.grid(row=4, column=0, padx=(40, 0), sticky=W)

        self.label_fecha_nacimiento_personal_salud = Label(self.frame_registro_personal_salud, text='Fecha de nacimiento', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_fecha_nacimiento_personal_salud.grid(row=0, column=2, padx=(100, 20), sticky=W)
        self.label_tipo_personal_salud = Label(self.frame_registro_personal_salud, text='Ocupación', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_tipo_personal_salud.grid(row=1, column=2, padx=(100, 20), sticky=W)
        self.label_sexo_personal_salud = Label(self.frame_registro_personal_salud, text='Sexo', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_sexo_personal_salud.grid(row=2, column=2, padx=(100, 20), sticky=W)
        self.label_email_personal_salud = Label(self.frame_registro_personal_salud, text='Email', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_email_personal_salud.grid(row=3, column=2, padx=(100, 20), sticky=W)
        self.label_disponibilidad = Label(self.frame_registro_personal_salud, text='Disponibilidad', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_disponibilidad.grid(row=4, column=2, padx=(100, 20), sticky=W)
        
        self.cuadro_dni_personal_salud = Entry(self.frame_registro_personal_salud, text='DNI', font=('Times New Roman', 10, 'bold'))
        self.cuadro_dni_personal_salud.grid(row=0, column=1)
        self.cuadro_nombres_personal_salud = Entry(self.frame_registro_personal_salud, font=('Times New Roman', 10, 'bold'))
        self.cuadro_nombres_personal_salud.grid(row=1, column=1)
        self.cuadro_apellido_paterno_personal_salud = Entry(self.frame_registro_personal_salud, font=('Times New Roman', 10, 'bold'))
        self.cuadro_apellido_paterno_personal_salud.grid(row=2, column=1)
        self.cuadro_apellido_materno_personal_salud = Entry(self.frame_registro_personal_salud, font=('Times New Roman', 10, 'bold'))
        self.cuadro_apellido_materno_personal_salud.grid(row=3, column=1)
        self.cuadro_telefono_personal_salud = Entry(self.frame_registro_personal_salud, font=('Times New Roman', 10, 'bold'))
        self.cuadro_telefono_personal_salud.grid(row=4, column=1)
        
        self.cuadro_fecha_nacimiento_personal_salud = Entry(self.frame_registro_personal_salud, font=('Times New Roman', 10, 'bold'), width=25)
        self.cuadro_fecha_nacimiento_personal_salud.grid(row=0, column=3, padx=(20, 0), sticky=W)
        self.opciones_ocupacion = ttk.Combobox(self.frame_registro_personal_salud, state='readonly', values=['Médico', 'Enfermero'], font=('Times New Roman', 10, 'bold'), width=22)
        self.opciones_ocupacion.set('Seleccione su ocupación')
        self.opciones_ocupacion.grid(row=1, column=3, padx=(20, 0), sticky=W)
        self.opciones_sexo_personal_salud = ttk.Combobox(self.frame_registro_personal_salud, state='readonly', values=['Masculino', 'Femenino'], font=('Times New Roman', 10, 'bold'), width=22)
        self.opciones_sexo_personal_salud.set('Seleccione su sexo')
        self.opciones_sexo_personal_salud.grid(row=2, column=3, padx=(20, 0), sticky=W)
        self.cuadro_email_personal_salud = Entry(self.frame_registro_personal_salud, font=('Times New Roman', 10, 'bold'), width=25)
        self.cuadro_email_personal_salud.grid(row=3, column=3, padx=(20, 0), sticky=W)
        self.opciones_disponibilidad = ttk.Combobox(self.frame_registro_personal_salud, state='readonly', values=['Mañana', 'Tarde', 'Noche'], font=('Times New Roman', 10, 'bold'), width=22)
        self.opciones_disponibilidad.set('Seleccione su disponibilidad')
        self.opciones_disponibilidad.grid(row=4, column=3, padx=(20, 0), sticky=W)

        self.frame_opciones_registro_medicos = Frame(self.frame_registro_personal_salud)
        self.frame_opciones_registro_medicos.config(bg='#0EB06E', pady=20)
        self.frame_opciones_registro_medicos.grid(row=5, column=0, columnspan=5, ipadx=50)

        self.opcion_limpiar_personal_salud = Button(self.frame_opciones_registro_medicos, text='Limpiar', cursor='hand2')
        self.opcion_limpiar_personal_salud.grid(row=0, column=0, padx=70)

        self.opcion_registrar_personal_salud = Button(self.frame_opciones_registro_medicos, text='Registrar', cursor='hand2')
        self.opcion_registrar_personal_salud.grid(row=0, column=1, padx=70)

        self.opcion_modificar_personal_salud = Button(self.frame_opciones_registro_medicos, text='Modificar', cursor='hand2')
        self.opcion_modificar_personal_salud.grid(row=0, column=2, padx=70)

        self.opcion_eliminar_personal_salud = Button(self.frame_opciones_registro_medicos, text='Eliminar', cursor='hand2')
        self.opcion_eliminar_personal_salud.grid(row=0, column=3, padx=70)

        def tabla_medicos():

            tabla_personal_salud = ttk.Treeview(self.frame_registro_personal_salud, columns=('DNI',
            'Nombres', 'Apellido paterno', 'Apellido materno', 'Teléfono', 'Fecha de nacimiento',
            'Ocupación', 'Sexo', 'Email', 'Disponibilidad'), height=3)
        
            tabla_personal_salud.column('#0', width=50, anchor=CENTER)
            tabla_personal_salud.column('DNI', width=60, anchor=CENTER)
            tabla_personal_salud.column('Nombres', width=60, anchor=CENTER)
            tabla_personal_salud.column('Apellido paterno', width=80, anchor=CENTER)
            tabla_personal_salud.column('Apellido materno', width=80, anchor=CENTER)
            tabla_personal_salud.column('Teléfono', width=60, anchor=CENTER)
            tabla_personal_salud.column('Fecha de nacimiento', width=120, anchor=CENTER)
            tabla_personal_salud.column('Ocupación', width=60, anchor=CENTER)
            tabla_personal_salud.column('Sexo', width=40, anchor=CENTER)
            tabla_personal_salud.column('Email', width=50, anchor=CENTER)
            tabla_personal_salud.column('Disponibilidad', width=100, anchor=CENTER)
            tabla_personal_salud.config(padding=(5, 10))
            tabla_personal_salud.grid(row=6, column=0, columnspan=4, padx=(40, 0))

            tabla_personal_salud.heading('#0', text='ID')
            tabla_personal_salud.heading('#1', text='DNI')
            tabla_personal_salud.heading('#2', text='Nombres')
            tabla_personal_salud.heading('#3', text='Apellido paterno')
            tabla_personal_salud.heading('#4', text='Apellido materno')
            tabla_personal_salud.heading('#5', text='Teléfono')
            tabla_personal_salud.heading('#6', text='Fecha de nacimiento')
            tabla_personal_salud.heading('#7', text='Ocupación')
            tabla_personal_salud.heading('#8', text='Sexo')
            tabla_personal_salud.heading('#9', text='Email')
            tabla_personal_salud.heading('#10', text='Disponibilidad')

            scroll_vertical_tabla_personal_salud = Scrollbar(self.frame_registro_personal_salud, command=tabla_personal_salud.yview)
            scroll_vertical_tabla_personal_salud.grid(row=6, column=4, sticky=NS, padx=(0, 10))
            tabla_personal_salud.configure(yscrollcommand=scroll_vertical_tabla_personal_salud.set)

        tabla_medicos()

    def ventana_inicio(self):
        if MenuEmssamlud.contador_frame_paciente >= 1:
            self.frame_registro_pacientes.destroy()
        if MenuEmssamlud.contador_frame_inicio >= 1:
            self.frame_opciones_inicio.destroy()
        if MenuEmssamlud.contador_frame_personal_salud >= 1:
            self.frame_registro_personal_salud.destroy()
        if MenuEmssamlud.contador_frame_agendar_cita >= 1:
            self.frame_agendar_cita.destroy()
                
        MenuEmssamlud.contador_frame_inicio += 1

        self.frame_opciones_inicio = Frame(self.ventana_principal)
        self.frame_opciones_inicio.config(bg='#0EB06E', padx=10, pady=20)
        self.frame_opciones_inicio.place(x=325, y=80)
        self.label_pacientes = Label(self.frame_opciones_inicio, text='Pacientes', font=('Times New Roman', 18, 'bold'), bg='#0EB06E')#, bg='#9DE8E2', fg='#C75819')
        self.label_pacientes.grid(row=0, column=0, padx=120, pady=(10, 20))
        self.imagen_pacientes = PhotoImage(file="imagenes/logo_pacientes.png")
        Button(self.frame_opciones_inicio, image=self.imagen_pacientes, bg='#9DE8E2', cursor='hand2', command=self.crear_frame_paciente).grid(row=1, column=0, padx=60)
        
        self.label_medicos = Label(self.frame_opciones_inicio, text='Personal de Salud', font=('Times New Roman', 18, 'bold'), bg='#0EB06E')
        self.label_medicos.grid(row=0, column=1, padx=(93, 105), pady=(10, 20))
        self.imagen_medicos = PhotoImage(file="imagenes/logo_personal_salud.png")
        Button(self.frame_opciones_inicio, image=self.imagen_medicos, bg='#9DE8E2', cursor='hand2', command=self.crear_frame_registro_personal_salud).grid(row=1, column=1)

    def crear_frame_agendar_cita(self):
        if MenuEmssamlud.contador_frame_agendar_cita >= 1:
            self.frame_agendar_cita.destroy()

        if MenuEmssamlud.contador_frame_inicio >= 1:
            self.frame_opciones_inicio.destroy()

        if MenuEmssamlud.contador_frame_paciente >= 1:
            self.frame_registro_pacientes.destroy()

        if MenuEmssamlud.contador_frame_personal_salud >= 1:
            self.frame_registro_personal_salud.destroy()

        MenuEmssamlud.contador_frame_agendar_cita += 1

        self.frame_opciones_inicio.destroy()
        self.frame_agendar_cita = Frame(self.ventana_principal)
        self.frame_agendar_cita.config(bg='#0EB06E', padx=10, pady=20)
        self.frame_agendar_cita.grid(row=0, column=3, rowspan=6)

        self.label_agendar_dni_paciente = Label(self.frame_agendar_cita, text='DNI Paciente', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_agendar_dni_paciente.grid(row=0, column=0, padx=(20, 0), sticky=W)
        self.label_agendar_dni_medico = Label(self.frame_agendar_cita, text='DNI Médico', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_agendar_dni_medico.grid(row=1, column=0, padx=(20, 0), sticky=W)
        self.label_fecha_cita = Label(self.frame_agendar_cita, text='Fecha de la cita', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_fecha_cita.grid(row=2, column=0, padx=(20, 0), sticky=W)
        self.label_precio_cita = Label(self.frame_agendar_cita, text='Precio de la cita', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_precio_cita.grid(row=3, column=0, padx=(20, 0), sticky=W)
        self.label_estado_cita = Label(self.frame_agendar_cita, text='Estado de la cita', font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_estado_cita.grid(row=4, column=0, padx=(20, 0), sticky=W)
        
        self.cuadro_agendar_dni_paciente = Entry(self.frame_agendar_cita, text='DNI', font=('Times New Roman', 10, 'bold'), width=25)
        self.cuadro_agendar_dni_paciente.grid(row=0, column=1, sticky=W)
        self.cuadro_agendar_dni_medico = Entry(self.frame_agendar_cita, font=('Times New Roman', 10, 'bold'), width=25)
        self.cuadro_agendar_dni_medico.grid(row=1, column=1, sticky=W)
        self.cuadro_fecha_cita = Entry(self.frame_agendar_cita, font=('Times New Roman', 10, 'bold'), width=25)
        self.cuadro_fecha_cita.grid(row=2, column=1, sticky=W)
        self.cuadro_precio_cita = Entry(self.frame_agendar_cita, font=('Times New Roman', 10, 'bold'), width=25)
        self.cuadro_precio_cita.grid(row=3, column=1, sticky=W)
        self.opciones_estado_cita = ttk.Combobox(self.frame_agendar_cita, state='readonly', values=['Atención pendiente', 'Atención confirmada'], font=('Times New Roman', 10, 'bold'), width=23)
        self.opciones_estado_cita.set('Seleccione el estado de la cita')
        self.opciones_estado_cita.grid(row=4, column=1, sticky=W)

        self.imagen_agendar_cita = PhotoImage(file='imagenes/logo_frame_agendar_cita.png')
        self.label_imagen_agendar_cita = Label(self.frame_agendar_cita, image=self.imagen_agendar_cita, bg='#0EB06E')
        self.label_imagen_agendar_cita.grid(row=0, column=2, rowspan=5, columnspan=3, sticky=W)

        self.frame_opciones_registro_medicos = Frame(self.frame_agendar_cita)
        self.frame_opciones_registro_medicos.config(bg='#0EB06E', pady=20)
        self.frame_opciones_registro_medicos.grid(row=5, column=0, columnspan=5, ipadx=50)

        self.opcion_nuevo_medico = Button(self.frame_opciones_registro_medicos, text='Limpiar', cursor='hand2')
        self.opcion_nuevo_medico.grid(row=0, column=0, padx=70)

        self.opcion_guardar_medico = Button(self.frame_opciones_registro_medicos, text='Registrar', cursor='hand2')
        self.opcion_guardar_medico.grid(row=0, column=1, padx=70)

        self.opcion_modificar_medico = Button(self.frame_opciones_registro_medicos, text='Modificar', cursor='hand2')
        self.opcion_modificar_medico.grid(row=0, column=2, padx=70)

        self.opcion_eliminar_medico = Button(self.frame_opciones_registro_medicos, text='Eliminar', cursor='hand2')
        self.opcion_eliminar_medico.grid(row=0, column=3, padx=70)

    def disenno_interfaz_menu_principal(self):
        self.ventana_principal = Frame(self)
        self.ventana_principal.config(bg='#9DE8E2')
        self.ventana_principal.pack(fill=BOTH, expand=True, pady=40)

        self.titulo_ventana = Label(self, text='Sistema de citas médicas - Emsamlud', bg='#0EB06E' ,font=('Times New Roman', 18, 'bold'), padx=100)
        self.titulo_ventana.place(x=330, y=4)

        self.logo_admin = PhotoImage(file='imagenes/logo_admin.png')
        self.cuadro_logo_admin = Label(self.ventana_principal, image=self.logo_admin, bg='#9DE8E2')
        self.cuadro_logo_admin.grid(row=0, column=0, columnspan=2, padx=(33, 0), sticky=S)
        self.cuadro_admin = Label(self.ventana_principal, text='Administrador', bg='#9DE8E2', fg='#117E5E', font=('Times New Roman', 18, 'bold'))
        self.cuadro_admin.grid(row=1, column=0, columnspan=2, padx=(30, 0), sticky=N)

        self.separador_horizontal = Frame(self.ventana_principal)
        self.separador_horizontal.config(bg='#0EB06E', height=12, width=228)
        self.separador_horizontal.place(x=0, y=217)

        self.ventana_inicio()

    def menu_opciones(self):
        self.imagen_opcion_inicio = PhotoImage(file="imagenes/logo_inicio.png")
        self.boton_inicio = Button(self.ventana_principal, image=self.imagen_opcion_inicio, command=self.ventana_inicio, cursor='hand2', height=38, width=98)
        self.boton_inicio.grid(row=2, column=0, columnspan=2, padx=(35, 0), sticky=N)

        self.imagen_opcion_agendar_cita = PhotoImage(file="imagenes/logo_agendar_cita.png")
        self.boton_agendar_cita = Button(self.ventana_principal, image=self.imagen_opcion_agendar_cita, cursor='hand2', height=38, width=98, command=self.crear_frame_agendar_cita)
        self.boton_agendar_cita.grid(row=3, column=0, columnspan=2, padx=(35, 0), sticky=N)

        self.imagen_opcion_atender_cita = PhotoImage(file="imagenes/logo_atender_cita.png")
        self.boton_atender_cita = Button(self.ventana_principal, image=self.imagen_opcion_atender_cita, cursor='hand2', height=38, width=98)
        self.boton_atender_cita.grid(row=4, column=0, columnspan=2, padx=(35, 0), sticky=N)

        self.imagen_opcion_reportes = PhotoImage(file="imagenes/logo_reportes.png")
        self.boton_reportes = Button(self.ventana_principal, image=self.imagen_opcion_reportes, cursor='hand2', height=38, width=98)
        self.boton_reportes.grid(row=5, column=0, columnspan=2, padx=(35, 0), sticky=N)

        self.separador_vertical = Label(self.ventana_principal)
        self.separador_vertical.config(bg='#0EB06E', height=35, width=1)
        self.separador_vertical.grid(row=0, column=2, rowspan=6, padx=40)