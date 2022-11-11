from tkinter import *
import tkinter.ttk as ttk
from tkcalendar import DateEntry
import util.centrar_ventana as pv
from datetime import datetime, date
from tkinter import messagebox
import clases.paciente as p
import clases.admin as adm


class MenuEmssamlud(Toplevel):
    contador_frame_inicio = 0
    contador_frame_paciente = 0
    contador_frame_personal_salud = 0
    contador_frame_agendar_cita = 0
    contador_frame_atender_cita = 0

    def __init__(self):
        super().__init__()
        self.geometry('1200x600')
        pv.centrar_ventana(self, 1200, 600)
        self.title('Emsamlud - Sistema')
        self.config(bg='#0EB06E')
        self.resizable(False, False)
        self.disenno_interfaz_menu_principal()
        self.menu_opciones()

    def crear_frame_paciente(self):
        self.id_paciente = None
        self.dni_paciente = None
        self.frame_opciones_inicio.destroy()
        MenuEmssamlud.contador_frame_paciente += 1

        self.frame_registro_pacientes = Frame(self.ventana_principal)
        self.frame_registro_pacientes.config(bg='#0EB06E', padx=10, pady=20)
        self.frame_registro_pacientes.grid(row=0, column=3, rowspan=6)

        self.label_dni_paciente = Label(self.frame_registro_pacientes, text='DNI', font=('Times New Roman', 10, 'bold'),
                                        height=3, bg='#0EB06E')
        self.label_dni_paciente.grid(row=0, column=0, padx=(40, 20), sticky=W)
        self.label_nombres_paciente = Label(self.frame_registro_pacientes, text='Nombres',
                                            font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_nombres_paciente.grid(row=1, column=0, padx=(40, 20), sticky=W)
        self.label_apellido_paterno_paciente = Label(self.frame_registro_pacientes, text='Apellido paterno',
                                                     font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_apellido_paterno_paciente.grid(row=2, column=0, padx=(40, 20), sticky=W)
        self.label_apellido_materno_paciente = Label(self.frame_registro_pacientes, text='Apellido materno',
                                                     font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_apellido_materno_paciente.grid(row=3, column=0, padx=(40, 20), sticky=W)
        self.label_telefono_paciente = Label(self.frame_registro_pacientes, text='Teléfono',
                                             font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_telefono_paciente.grid(row=4, column=0, padx=(40, 0), sticky=W)

        self.label_fecha_nacimiento_paciente = Label(self.frame_registro_pacientes, text='Fecha de nacimiento',
                                                     font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_fecha_nacimiento_paciente.grid(row=0, column=2, padx=(100, 20), sticky=W)
        self.label_direccion_paciente = Label(self.frame_registro_pacientes, text='Direccion',
                                              font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_direccion_paciente.grid(row=1, column=2, padx=(100, 20), sticky=W)
        self.label_sexo_paciente = Label(self.frame_registro_pacientes, text='Sexo',
                                         font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_sexo_paciente.grid(row=2, column=2, padx=(100, 20), sticky=W)
        self.label_email_paciente = Label(self.frame_registro_pacientes, text='Email',
                                          font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_email_paciente.grid(row=3, column=2, padx=(100, 20), sticky=W)
        self.label_observacion = Label(self.frame_registro_pacientes, text='Observación',
                                       font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_observacion.grid(row=4, column=2, padx=(100, 20), sticky=W)

        self.cuadro_dni_paciente = Entry(self.frame_registro_pacientes, text='DNI',
                                         font=('Times New Roman', 10, 'bold'), state=DISABLED)
        self.cuadro_dni_paciente.grid(row=0, column=1)
        self.cuadro_nombres_paciente = Entry(self.frame_registro_pacientes, font=('Times New Roman', 10, 'bold'),
                                             state=DISABLED)
        self.cuadro_nombres_paciente.grid(row=1, column=1)
        self.cuadro_apellido_paterno_paciente = Entry(self.frame_registro_pacientes,
                                                      font=('Times New Roman', 10, 'bold'), state=DISABLED)
        self.cuadro_apellido_paterno_paciente.grid(row=2, column=1)
        self.cuadro_apellido_materno_paciente = Entry(self.frame_registro_pacientes,
                                                      font=('Times New Roman', 10, 'bold'), state=DISABLED)
        self.cuadro_apellido_materno_paciente.grid(row=3, column=1)
        self.cuadro_telefono_paciente = Entry(self.frame_registro_pacientes, font=('Times New Roman', 10, 'bold'),
                                              state=DISABLED)
        self.cuadro_telefono_paciente.grid(row=4, column=1)

        self.cuadro_fecha_nacimiento_paciente = DateEntry(self.frame_registro_pacientes, locale='es_ES',
                                                          date_pattern='dd/MM/yyyy')
        self.cuadro_fecha_nacimiento_paciente.state([DISABLED])

        self.lista_fechas = []
        self.fecha_inicial = datetime.strftime(self.cuadro_fecha_nacimiento_paciente.get_date(), '%Y-%m-%d')
        self.lista_fechas.append(self.fecha_inicial)

        def almacenar_fechas(e):
            fecha_seleccionada = datetime.strftime(self.cuadro_fecha_nacimiento_paciente.get_date(), '%Y-%m-%d')
            self.lista_fechas.append(fecha_seleccionada)

        self.cuadro_fecha_nacimiento_paciente.bind("<<DateEntrySelected>>", almacenar_fechas)
        self.cuadro_fecha_nacimiento_paciente.grid(row=0, column=3, padx=(20, 0), sticky=W)

        self.cuadro_direccion_paciente = Entry(self.frame_registro_pacientes, font=('Times New Roman', 10, 'bold'),
                                               width=25, state=DISABLED)
        self.cuadro_direccion_paciente.grid(row=1, column=3, padx=(20, 0), sticky=W)

        self.estado_sexo = False
        self.cuadro_sexo_paciente = ttk.Combobox(self.frame_registro_pacientes, state=DISABLED,
                                                 values=['Masculino', 'Femenino'], font=('Times New Roman', 10, 'bold'),
                                                 width=23)
        self.cuadro_sexo_paciente.grid(row=2, column=3, padx=(20, 0), sticky=W)
        self.cuadro_sexo_paciente.set('Seleccione su sexo')

        self.cuadro_email_paciente = Entry(self.frame_registro_pacientes, font=('Times New Roman', 10, 'bold'),
                                           width=25, state=DISABLED)
        self.cuadro_email_paciente.grid(row=3, column=3, padx=(20, 0), sticky=W)

        self.frame_obs = Frame(self.frame_registro_pacientes, bg='#0EB06E', height=100)
        self.frame_obs.grid(row=4, column=3, padx=(20, 0), sticky=W, columnspan=2)

        self.cuadro_observacion = Text(self.frame_obs, font=('Times New Roman', 10, 'bold'), width=25, height=3.5,
                                       state=DISABLED)
        self.cuadro_observacion.grid(row=0, column=0, sticky=W)

        self.scroll_cuadro_observacion = Scrollbar(self.frame_obs, command=self.cuadro_observacion.yview)
        self.scroll_cuadro_observacion.grid(row=0, column=1, sticky=NS, padx=10)
        self.cuadro_observacion.config(yscrollcommand=self.scroll_cuadro_observacion.set)

        def habilitar_botones():
            self.opcion_registrar_paciente.config(state=NORMAL)
            self.opcion_modificar_paciente.config(state=NORMAL)
            self.opcion_eliminar_paciente.config(state=NORMAL)

        def deshabilitar_botones():
            self.opcion_registrar_paciente.config(state=DISABLED)
            self.opcion_modificar_paciente.config(state=DISABLED)
            self.opcion_eliminar_paciente.config(state=DISABLED)

        def nuevo():
            habilitar_botones()
            self.cuadro_dni_paciente.config(state=NORMAL)
            self.cuadro_nombres_paciente.config(state=NORMAL)
            self.cuadro_apellido_paterno_paciente.config(state=NORMAL)
            self.cuadro_apellido_materno_paciente.config(state=NORMAL)
            self.cuadro_telefono_paciente.config(state=NORMAL)
            self.cuadro_fecha_nacimiento_paciente.config(state=[ACTIVE])
            self.cuadro_direccion_paciente.config(state=NORMAL)
            self.estado_sexo = True
            self.cuadro_sexo_paciente.config(state=NORMAL)
            self.cuadro_email_paciente.config(state=NORMAL)
            self.cuadro_observacion.config(state=NORMAL)

            self.cuadro_dni_paciente.delete('0', 'end')
            self.cuadro_nombres_paciente.delete('0', 'end')
            self.cuadro_apellido_paterno_paciente.delete('0', 'end')
            self.cuadro_apellido_materno_paciente.delete('0', 'end')
            self.cuadro_telefono_paciente.delete('0', 'end')
            self.cuadro_direccion_paciente.delete('0', 'end')
            self.cuadro_sexo_paciente.set('Seleccione su sexo')
            self.cuadro_email_paciente.delete('0', 'end')
            self.cuadro_observacion.delete('1.0', 'end')

        def dia_fecha_seleccionada(fecha):
            return int(fecha[8] + fecha[9])

        def mes_fecha_seleccionada(fecha):
            return int(fecha[5] + fecha[6])

        def anio_fecha_seleccionada(fecha):
            return (int(fecha[0] + fecha[1] +
                        fecha[2] + fecha[3]))

        self.fecha_actual = datetime.strftime(date.today(), '%Y-%m-%d')

        def deshabilitar_campos():
            self.cuadro_dni_paciente.delete('0', 'end')
            self.cuadro_nombres_paciente.delete('0', 'end')
            self.cuadro_apellido_paterno_paciente.delete('0', 'end')
            self.cuadro_apellido_materno_paciente.delete('0', 'end')
            self.cuadro_telefono_paciente.delete('0', 'end')
            self.cuadro_fecha_nacimiento_paciente.set_date(date(anio_fecha_seleccionada(self.fecha_actual),
                                                                mes_fecha_seleccionada(self.fecha_actual),
                                                                dia_fecha_seleccionada(self.fecha_actual)))
            self.cuadro_direccion_paciente.delete('0', 'end')
            self.cuadro_sexo_paciente.set('Seleccione su sexo')
            self.cuadro_email_paciente.delete('0', 'end')
            self.cuadro_observacion.delete('1.0', 'end')

            self.cuadro_dni_paciente.config(state=DISABLED)
            self.cuadro_nombres_paciente.config(state=DISABLED)
            self.cuadro_apellido_paterno_paciente.config(state=DISABLED)
            self.cuadro_apellido_materno_paciente.config(state=DISABLED)
            self.cuadro_telefono_paciente.config(state=DISABLED)
            self.cuadro_fecha_nacimiento_paciente.config(state=[DISABLED])
            self.cuadro_direccion_paciente.config(state=DISABLED)
            self.estado_sexo = False
            self.cuadro_sexo_paciente.config(state=DISABLED)
            self.cuadro_email_paciente.config(state=DISABLED)
            self.cuadro_observacion.config(state=DISABLED)

        self.error_ingreso_dni = False
        self.error_ingreso_telefono = False

        def verificar_errores_dni_telefono():
            try:
                int(self.cuadro_dni_paciente.get())
                self.error_ingreso_dni = False
            except:
                self.error_ingreso_dni = True
            try:
                int(self.cuadro_telefono_paciente.get())
                self.error_ingreso_telefono = False
            except:
                self.error_ingreso_telefono = True

        def registrar():
            admin = adm.Admin()
            verificar_errores_dni_telefono()
            if (len(self.cuadro_dni_paciente.get()) == 0 or not self.cuadro_nombres_paciente.get()
                    or not self.cuadro_apellido_paterno_paciente.get()
                    or not self.cuadro_apellido_materno_paciente.get() or len(self.cuadro_telefono_paciente.get()) == 0
                    or not self.cuadro_direccion_paciente.get() or self.cuadro_sexo_paciente.get() == 'Seleccione su sexo'):
                messagebox.showwarning('Advertencia', 'Debe llenar los campos obligatorios.')
            elif self.error_ingreso_dni == True and self.error_ingreso_telefono == True:
                messagebox.showwarning('Advertencia',
                                       'Verifique el DNI y el número telefónico ingresados (solo dígitos).')
            elif self.error_ingreso_dni == True and len(self.cuadro_telefono_paciente.get()) != 9:
                messagebox.showwarning('Advertencia',
                                       'Verifique el DNI (solo dígitos) y el número telefónico ingresado (9 dígitos).')
            elif len(self.cuadro_dni_paciente.get()) != 8 and self.error_ingreso_telefono == True:
                messagebox.showwarning('Advertencia',
                                       'Verifique el DNI (8 dígitos) y el número telefónico ingresado (solo dígitos).')
            elif self.error_ingreso_dni == True and self.error_ingreso_telefono == False:
                messagebox.showwarning('Advertencia', 'Verifique el DNI ingresado (solo dígitos).')
            elif self.error_ingreso_dni == False and self.error_ingreso_telefono == True:
                messagebox.showwarning('Advertencia', 'Verifique el número telefónico ingresado (solo dígitos).')
            elif len(self.cuadro_dni_paciente.get()) != 8 and len(self.cuadro_telefono_paciente.get()) == 9:
                messagebox.showwarning('Advertencia', 'Verifique el DNI ingresado (8 dígitos).')
            elif len(self.cuadro_telefono_paciente.get()) != 9 and len(self.cuadro_dni_paciente.get()) == 8:
                messagebox.showwarning('Advertencia', 'Verifique el número telefónico ingresado (9 dígitos).')
            elif len(self.cuadro_dni_paciente.get()) != 8 and len(self.cuadro_telefono_paciente.get()) != 9:
                messagebox.showwarning('Advertencia',
                                       'Verifique el DNI (8 dígitos) y el número telefónico ingresados (9 dígitos).')
            elif self.dni_paciente == int(self.cuadro_dni_paciente.get()):
                messagebox.showwarning('Advertencia', f'El paciente con DNI {self.dni_paciente} ya ha sido registrado.')
            else:
                paciente = p.Paciente(self.cuadro_dni_paciente.get(), self.cuadro_nombres_paciente.get(),
                                      self.cuadro_apellido_paterno_paciente.get(),
                                      self.cuadro_apellido_materno_paciente.get(),
                                      self.cuadro_telefono_paciente.get(), self.lista_fechas[-1],
                                      self.cuadro_direccion_paciente.get(), self.cuadro_sexo_paciente.get(),
                                      self.cuadro_email_paciente.get(),
                                      self.cuadro_observacion.get(1.0, "end-1c").replace('\n', ' '))

                admin.registrar_paciente(paciente)
                tabla_pacientes()
                deshabilitar_botones()
                deshabilitar_campos()

        def modificar():
            admin = adm.Admin()
            verificar_errores_dni_telefono()

            if self.id_paciente == None:
                messagebox.showwarning('Advertencia', 'No ha seleccionado un paciente para modificar.')
            elif (len(self.cuadro_dni_paciente.get()) == 0 or not self.cuadro_nombres_paciente.get()
                  or not self.cuadro_apellido_paterno_paciente.get()
                  or not self.cuadro_apellido_materno_paciente.get() or len(self.cuadro_telefono_paciente.get()) == 0
                  or not self.cuadro_direccion_paciente.get() or self.cuadro_sexo_paciente.get() == 'Seleccione su sexo'):
                messagebox.showwarning('Advertencia', 'Debe llenar los campos obligatorios.')
            elif self.error_ingreso_dni == True and self.error_ingreso_telefono == True:
                messagebox.showwarning('Advertencia',
                                       'Verifique el DNI y el número telefónico ingresados (solo dígitos).')
            elif self.error_ingreso_dni == True and len(self.cuadro_telefono_paciente.get()) != 9:
                messagebox.showwarning('Advertencia',
                                       'Verifique el DNI (solo dígitos) y el número telefónico ingresado (9 dígitos).')
            elif len(self.cuadro_dni_paciente.get()) != 8 and self.error_ingreso_telefono == True:
                messagebox.showwarning('Advertencia',
                                       'Verifique el DNI (8 dígitos) y el número telefónico ingresado (solo dígitos).')
            elif self.error_ingreso_dni == True and self.error_ingreso_telefono == False:
                messagebox.showwarning('Advertencia', 'Verifique el DNI ingresado (solo dígitos).')
            elif self.error_ingreso_dni == False and self.error_ingreso_telefono == True:
                messagebox.showwarning('Advertencia', 'Verifique el número telefónico ingresado (solo dígitos).')
            elif len(self.cuadro_dni_paciente.get()) != 8 and len(self.cuadro_telefono_paciente.get()) == 9:
                messagebox.showwarning('Advertencia', 'Verifique el DNI ingresado (8 dígitos).')
            elif len(self.cuadro_telefono_paciente.get()) != 9 and len(self.cuadro_dni_paciente.get()) == 8:
                messagebox.showwarning('Advertencia', 'Verifique el número telefónico ingresado (9 dígitos).')
            elif len(self.cuadro_dni_paciente.get()) != 8 and len(self.cuadro_telefono_paciente.get()) != 9:
                messagebox.showwarning('Advertencia',
                                       'Verifique el DNI (8 dígitos) y el número telefónico ingresados (9 dígitos).')
            else:
                paciente = p.Paciente(self.cuadro_dni_paciente.get(), self.cuadro_nombres_paciente.get(),
                                      self.cuadro_apellido_paterno_paciente.get(),
                                      self.cuadro_apellido_materno_paciente.get(),
                                      self.cuadro_telefono_paciente.get(), self.lista_fechas[-1],
                                      self.cuadro_direccion_paciente.get(), self.cuadro_sexo_paciente.get(),
                                      self.cuadro_email_paciente.get(),
                                      self.cuadro_observacion.get(1.0, "end-1c").replace('\n', ' '))

                admin.modificar_paciente(paciente, self.id_paciente)
                tabla_pacientes()
                deshabilitar_botones()
                deshabilitar_campos()

        def eliminar():
            admin = adm.Admin()
            verificar_errores_dni_telefono()
            if self.id_paciente == None:
                messagebox.showwarning('Advertencia', 'No ha seleccionado un paciente para eliminar.')
            elif self.error_ingreso_dni == True or self.dni_paciente != int(self.cuadro_dni_paciente.get()):
                deshabilitar_campos()
                self.cuadro_dni_paciente.config(state=NORMAL)
                self.cuadro_dni_paciente.insert('0', self.dni_paciente)
                messagebox.showwarning('Advertencia', 'El DNI del paciente a eliminar no coincide con el seleccionado.')
            else:
                admin.eliminar_paciente(self.id_paciente)
                tabla_pacientes()
                deshabilitar_botones()
                deshabilitar_campos()

        self.frame_opciones_registro_pacientes = Frame(self.frame_registro_pacientes)
        self.frame_opciones_registro_pacientes.config(bg='#0EB06E', pady=20)
        self.frame_opciones_registro_pacientes.grid(row=5, column=0, columnspan=5, ipadx=50)

        self.opcion_nuevo_paciente = Button(self.frame_opciones_registro_pacientes, text='Nuevo', cursor='hand2',
                                            command=nuevo)
        self.opcion_nuevo_paciente.grid(row=0, column=0, padx=70)

        self.opcion_registrar_paciente = Button(self.frame_opciones_registro_pacientes, text='Registrar',
                                                cursor='hand2', command=registrar, state=DISABLED)
        self.opcion_registrar_paciente.grid(row=0, column=1, padx=70)

        self.opcion_modificar_paciente = Button(self.frame_opciones_registro_pacientes, text='Modificar',
                                                cursor='hand2', command=modificar, state=DISABLED)
        self.opcion_modificar_paciente.grid(row=0, column=2, padx=70)

        self.opcion_eliminar_paciente = Button(self.frame_opciones_registro_pacientes, text='Eliminar', cursor='hand2',
                                               command=eliminar, state=DISABLED)
        self.opcion_eliminar_paciente.grid(row=0, column=3, padx=70)

        def tabla_pacientes():
            tabla_pacientes = ttk.Treeview(self.frame_registro_pacientes, columns=('DNI', 'Nombres',
                                                                                   'Apellido paterno',
                                                                                   'Apellido materno', 'Teléfono',
                                                                                   'Fecha de nacimiento',
                                                                                   'Dirección', 'Sexo', 'Email',
                                                                                   'Observación'), height=3)

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

            admin = adm.Admin()
            datos_paciente = admin.listar_datos_paciente()

            for dato in datos_paciente:
                tabla_pacientes.insert('', END, text=dato[0], values=(dato[1], dato[2],
                                                                      dato[3], dato[4], dato[5], dato[6], dato[7],
                                                                      dato[8], dato[9], dato[10]))

            def paciente_seleccionado(event):
                habilitar_botones()
                self.cuadro_dni_paciente.config(state=NORMAL)
                self.cuadro_nombres_paciente.config(state=NORMAL)
                self.cuadro_apellido_paterno_paciente.config(state=NORMAL)
                self.cuadro_apellido_materno_paciente.config(state=NORMAL)
                self.cuadro_telefono_paciente.config(state=NORMAL)
                self.cuadro_fecha_nacimiento_paciente.config(state=[ACTIVE])
                self.cuadro_direccion_paciente.config(state=NORMAL)
                self.estado_sexo = True
                self.cuadro_sexo_paciente.config(state=NORMAL)
                self.cuadro_email_paciente.config(state=NORMAL)
                self.cuadro_observacion.config(state=NORMAL)

                registro_seleccionado = tabla_pacientes.focus()
                if not registro_seleccionado:
                    return None
                data = tabla_pacientes.item(registro_seleccionado)
                self.id_paciente = data["text"]
                (self.dni_paciente, nombres_paciente, apellido_paterno_paciente, apellido_materno_paciente,
                 telefono_paciente, fecha_nacimiento_paciente, direccion_paciente, sexo_paciente,
                 email_paciente, observacion_paciente) = data["values"]

                self.cuadro_dni_paciente.delete('0', 'end')
                self.cuadro_dni_paciente.insert(0, self.dni_paciente)
                self.cuadro_nombres_paciente.delete('0', 'end')
                self.cuadro_nombres_paciente.insert(0, nombres_paciente)
                self.cuadro_apellido_paterno_paciente.delete('0', 'end')
                self.cuadro_apellido_paterno_paciente.insert(0, apellido_paterno_paciente)
                self.cuadro_apellido_materno_paciente.delete('0', 'end')
                self.cuadro_apellido_materno_paciente.insert(0, apellido_materno_paciente)
                self.cuadro_telefono_paciente.delete('0', 'end')
                self.cuadro_telefono_paciente.insert(0, telefono_paciente)
                self.cuadro_fecha_nacimiento_paciente.set_date(date(anio_fecha_seleccionada(fecha_nacimiento_paciente),
                                                                    mes_fecha_seleccionada(fecha_nacimiento_paciente),
                                                                    dia_fecha_seleccionada(fecha_nacimiento_paciente)))
                self.cuadro_direccion_paciente.delete('0', 'end')
                self.cuadro_direccion_paciente.insert(0, direccion_paciente)
                if self.estado_sexo:
                    self.cuadro_sexo_paciente.set(sexo_paciente)
                self.cuadro_email_paciente.delete('0', 'end')
                self.cuadro_email_paciente.insert(0, email_paciente)
                self.cuadro_observacion.delete('1.0', 'end')
                self.cuadro_observacion.insert('insert', observacion_paciente)

            tabla_pacientes.bind("<<TreeviewSelect>>", paciente_seleccionado)

        tabla_pacientes()

    def crear_frame_personal_salud(self):
        MenuEmssamlud.contador_frame_personal_salud += 1
        self.frame_opciones_inicio.destroy()
        self.frame_registro_personal_salud = Frame(self.ventana_principal)
        self.frame_registro_personal_salud.config(bg='#0EB06E', padx=10, pady=20)
        self.frame_registro_personal_salud.grid(row=0, column=3, rowspan=6)

        self.label_dni_personal_salud = Label(self.frame_registro_personal_salud, text='DNI',
                                              font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_dni_personal_salud.grid(row=0, column=0, padx=(40, 20), sticky=W)
        self.label_nombres_personal_salud = Label(self.frame_registro_personal_salud, text='Nombres',
                                                  font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_nombres_personal_salud.grid(row=1, column=0, padx=(40, 20), sticky=W)
        self.label_apellido_paterno_personal_salud = Label(self.frame_registro_personal_salud, text='Apellido paterno',
                                                           font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_apellido_paterno_personal_salud.grid(row=2, column=0, padx=(40, 20), sticky=W)
        self.label_apellido_materno_personal_salud = Label(self.frame_registro_personal_salud, text='Apellido materno',
                                                           font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_apellido_materno_personal_salud.grid(row=3, column=0, padx=(40, 20), sticky=W)
        self.label_telefono_personal_salud = Label(self.frame_registro_personal_salud, text='Teléfono',
                                                   font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_telefono_personal_salud.grid(row=4, column=0, padx=(40, 0), sticky=W)

        self.label_fecha_nacimiento_personal_salud = Label(self.frame_registro_personal_salud,
                                                           text='Fecha de nacimiento',
                                                           font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_fecha_nacimiento_personal_salud.grid(row=0, column=2, padx=(100, 20), sticky=W)
        self.label_tipo_personal_salud = Label(self.frame_registro_personal_salud, text='Ocupación',
                                               font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_tipo_personal_salud.grid(row=1, column=2, padx=(100, 20), sticky=W)
        self.label_sexo_personal_salud = Label(self.frame_registro_personal_salud, text='Sexo',
                                               font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_sexo_personal_salud.grid(row=2, column=2, padx=(100, 20), sticky=W)
        self.label_email_personal_salud = Label(self.frame_registro_personal_salud, text='Email',
                                                font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_email_personal_salud.grid(row=3, column=2, padx=(100, 20), sticky=W)
        self.label_disponibilidad = Label(self.frame_registro_personal_salud, text='Disponibilidad',
                                          font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_disponibilidad.grid(row=4, column=2, padx=(100, 20), sticky=W)

        self.cuadro_dni_personal_salud = Entry(self.frame_registro_personal_salud, text='DNI',
                                               font=('Times New Roman', 10, 'bold'))
        self.cuadro_dni_personal_salud.grid(row=0, column=1)
        self.cuadro_nombres_personal_salud = Entry(self.frame_registro_personal_salud,
                                                   font=('Times New Roman', 10, 'bold'))
        self.cuadro_nombres_personal_salud.grid(row=1, column=1)
        self.cuadro_apellido_paterno_personal_salud = Entry(self.frame_registro_personal_salud,
                                                            font=('Times New Roman', 10, 'bold'))
        self.cuadro_apellido_paterno_personal_salud.grid(row=2, column=1)
        self.cuadro_apellido_materno_personal_salud = Entry(self.frame_registro_personal_salud,
                                                            font=('Times New Roman', 10, 'bold'))
        self.cuadro_apellido_materno_personal_salud.grid(row=3, column=1)
        self.cuadro_telefono_personal_salud = Entry(self.frame_registro_personal_salud,
                                                    font=('Times New Roman', 10, 'bold'))
        self.cuadro_telefono_personal_salud.grid(row=4, column=1)

        self.cuadro_fecha_nacimiento_personal_salud = Entry(self.frame_registro_personal_salud,
                                                            font=('Times New Roman', 10, 'bold'), width=25)
        self.cuadro_fecha_nacimiento_personal_salud.grid(row=0, column=3, padx=(20, 0), sticky=W)
        self.opciones_ocupacion = ttk.Combobox(self.frame_registro_personal_salud, state='readonly',
                                               values=['Médico', 'Enfermero'], font=('Times New Roman', 10, 'bold'),
                                               width=22)
        self.opciones_ocupacion.set('Seleccione su ocupación')
        self.opciones_ocupacion.grid(row=1, column=3, padx=(20, 0), sticky=W)
        self.cuadro_sexo_personal_salud = ttk.Combobox(self.frame_registro_personal_salud, state='readonly',
                                                       values=['Masculino', 'Femenino'],
                                                       font=('Times New Roman', 10, 'bold'), width=22)
        self.cuadro_sexo_personal_salud.set('Seleccione su sexo')
        self.cuadro_sexo_personal_salud.grid(row=2, column=3, padx=(20, 0), sticky=W)
        self.cuadro_email_personal_salud = Entry(self.frame_registro_personal_salud,
                                                 font=('Times New Roman', 10, 'bold'), width=25)
        self.cuadro_email_personal_salud.grid(row=3, column=3, padx=(20, 0), sticky=W)
        self.opciones_disponibilidad = ttk.Combobox(self.frame_registro_personal_salud, state='readonly',
                                                    values=['Mañana', 'Tarde', 'Noche'],
                                                    font=('Times New Roman', 10, 'bold'), width=22)
        self.opciones_disponibilidad.set('Seleccione su disponibilidad')
        self.opciones_disponibilidad.grid(row=4, column=3, padx=(20, 0), sticky=W)

        self.frame_opciones_registro_medicos = Frame(self.frame_registro_personal_salud)
        self.frame_opciones_registro_medicos.config(bg='#0EB06E', pady=20)
        self.frame_opciones_registro_medicos.grid(row=5, column=0, columnspan=5, ipadx=50)

        self.opcion_limpiar_personal_salud = Button(self.frame_opciones_registro_medicos, text='Limpiar',
                                                    cursor='hand2')
        self.opcion_limpiar_personal_salud.grid(row=0, column=0, padx=70)

        self.opcion_registrar_personal_salud = Button(self.frame_opciones_registro_medicos, text='Registrar',
                                                      cursor='hand2')
        self.opcion_registrar_personal_salud.grid(row=0, column=1, padx=70)

        self.opcion_modificar_personal_salud = Button(self.frame_opciones_registro_medicos, text='Modificar',
                                                      cursor='hand2')
        self.opcion_modificar_personal_salud.grid(row=0, column=2, padx=70)

        self.opcion_eliminar_personal_salud = Button(self.frame_opciones_registro_medicos, text='Eliminar',
                                                     cursor='hand2')
        self.opcion_eliminar_personal_salud.grid(row=0, column=3, padx=70)

        self.tabla_personal_salud = ttk.Treeview(self.frame_registro_personal_salud, columns=(
        'DNI', 'Nombres', 'Apellido paterno', 'Apellido materno', 'Teléfono', 'Fecha de nacimiento', 'Ocupación',
        'Sexo', 'Email', 'Disponibilidad'), height=3)

        self.tabla_personal_salud.column('#0', width=50)
        self.tabla_personal_salud.column('DNI', width=60, anchor=CENTER)
        self.tabla_personal_salud.column('Nombres', width=60, anchor=CENTER)
        self.tabla_personal_salud.column('Apellido paterno', width=80, anchor=CENTER)
        self.tabla_personal_salud.column('Apellido materno', width=80, anchor=CENTER)
        self.tabla_personal_salud.column('Teléfono', width=60, anchor=CENTER)
        self.tabla_personal_salud.column('Fecha de nacimiento', width=120, anchor=CENTER)
        self.tabla_personal_salud.column('Ocupación', width=60, anchor=CENTER)
        self.tabla_personal_salud.column('Sexo', width=40, anchor=CENTER)
        self.tabla_personal_salud.column('Email', width=50, anchor=CENTER)
        self.tabla_personal_salud.column('Disponibilidad', width=100, anchor=CENTER)
        self.tabla_personal_salud.config(padding=(5, 10))

        self.tabla_personal_salud.grid(row=6, column=0, columnspan=4, padx=(40, 0))

        self.tabla_personal_salud.heading('#0', text='ID')
        self.tabla_personal_salud.heading('DNI', text='DNI')
        self.tabla_personal_salud.heading('Nombres', text='Nombres')
        self.tabla_personal_salud.heading('Apellido paterno', text='Apellido paterno')
        self.tabla_personal_salud.heading('Apellido materno', text='Apellido materno')
        self.tabla_personal_salud.heading('Teléfono', text='Teléfono')
        self.tabla_personal_salud.heading('Fecha de nacimiento', text='Fecha de nacimiento')
        self.tabla_personal_salud.heading('Ocupación', text='Ocupación')
        self.tabla_personal_salud.heading('Sexo', text='Sexo')
        self.tabla_personal_salud.heading('Email', text='Email')
        self.tabla_personal_salud.heading('Disponibilidad', text='Disponibilidad')

        self.scroll_vertical_tabla_personal_salud = Scrollbar(self.frame_registro_personal_salud,
                                                              command=self.tabla_personal_salud.yview)
        self.scroll_vertical_tabla_personal_salud.grid(row=6, column=4, sticky=NS, padx=(0, 90))
        self.tabla_personal_salud.configure(yscrollcommand=self.scroll_vertical_tabla_personal_salud.set)

    def ventana_inicio(self):
        if MenuEmssamlud.contador_frame_inicio >= 1:
            self.frame_opciones_inicio.destroy()
        if MenuEmssamlud.contador_frame_paciente >= 1:
            self.frame_registro_pacientes.destroy()
        if MenuEmssamlud.contador_frame_agendar_cita >= 1:
            self.frame_agendar_cita.destroy()
        if MenuEmssamlud.contador_frame_personal_salud >= 1:
            self.frame_registro_personal_salud.destroy()
        if MenuEmssamlud.contador_frame_atender_cita >= 1:
            self.frame_atender_cita.destroy()

        MenuEmssamlud.contador_frame_inicio += 1

        self.frame_opciones_inicio = Frame(self.ventana_principal)
        self.frame_opciones_inicio.config(bg='#0EB06E', padx=10, pady=20)
        self.frame_opciones_inicio.place(x=325, y=80)
        self.label_pacientes = Label(self.frame_opciones_inicio, text='Pacientes', font=('Times New Roman', 18, 'bold'),
                                     bg='#0EB06E')
        self.label_pacientes.grid(row=0, column=0, padx=120, pady=(10, 20))
        self.imagen_pacientes = PhotoImage(file="imagenes/logo_pacientes.png")
        Button(self.frame_opciones_inicio, image=self.imagen_pacientes, bg='#9DE8E2', command=self.crear_frame_paciente,
               cursor='hand2').grid(row=1, column=0, padx=60)

        self.label_medicos = Label(self.frame_opciones_inicio, text='Personal de Salud',
                                   font=('Times New Roman', 18, 'bold'), bg='#0EB06E')
        self.label_medicos.grid(row=0, column=1, padx=(93, 105), pady=(10, 20))
        self.imagen_medicos = PhotoImage(file="imagenes/logo_personal_salud.png")
        Button(self.frame_opciones_inicio, image=self.imagen_medicos, bg='#9DE8E2',
               command=self.crear_frame_personal_salud, cursor='hand2').grid(row=1, column=1)

    def crear_frame_agendar_cita(self):
        if MenuEmssamlud.contador_frame_agendar_cita >= 1:
            self.frame_agendar_cita.destroy()

        if MenuEmssamlud.contador_frame_inicio >= 1:
            self.frame_opciones_inicio.destroy()

        if MenuEmssamlud.contador_frame_paciente >= 1:
            self.frame_registro_pacientes.destroy()

        if MenuEmssamlud.contador_frame_personal_salud >= 1:
            self.frame_registro_personal_salud.destroy()

        if MenuEmssamlud.contador_frame_atender_cita >= 1:
            self.frame_atender_cita.destroy()

        MenuEmssamlud.contador_frame_agendar_cita += 1

        self.contador_abrir_calendario = 0

        self.frame_opciones_inicio.destroy()
        self.frame_agendar_cita = Frame(self.ventana_principal)
        self.frame_agendar_cita.config(bg='#0EB06E', padx=10, pady=20)
        self.frame_agendar_cita.grid(row=0, column=3, rowspan=6)

        self.label_agendar_dni_paciente = Label(self.frame_agendar_cita, text='DNI Paciente',
                                                font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_agendar_dni_paciente.grid(row=0, column=0, padx=(20, 0), sticky=W)
        self.label_agendar_dni_medico = Label(self.frame_agendar_cita, text='DNI Médico',
                                              font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_agendar_dni_medico.grid(row=1, column=0, padx=(20, 0), sticky=W)
        self.label_fecha_cita = Label(self.frame_agendar_cita, text='Fecha de la cita',
                                      font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_fecha_cita.grid(row=2, column=0, padx=(20, 0), sticky=W)
        self.label_precio_cita = Label(self.frame_agendar_cita, text='Precio de la cita',
                                       font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_precio_cita.grid(row=3, column=0, padx=(20, 0), sticky=W)
        self.label_estado_cita = Label(self.frame_agendar_cita, text='Estado de la cita',
                                       font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_estado_cita.grid(row=4, column=0, padx=(20, 0), sticky=W)

        self.cuadro_agendar_dni_paciente = Entry(self.frame_agendar_cita, text='DNI',
                                                 font=('Times New Roman', 10, 'bold'), width=25)
        self.cuadro_agendar_dni_paciente.grid(row=0, column=1, sticky=W)
        self.cuadro_agendar_dni_medico = Entry(self.frame_agendar_cita, font=('Times New Roman', 10, 'bold'), width=25)
        self.cuadro_agendar_dni_medico.grid(row=1, column=1, sticky=W)
        self.cuadro_fecha_cita = Entry(self.frame_agendar_cita, font=('Times New Roman', 10, 'bold'), width=25)
        self.cuadro_fecha_cita.grid(row=2, column=1, sticky=W)
        self.cuadro_precio_cita = Entry(self.frame_agendar_cita, font=('Times New Roman', 10, 'bold'), width=25)
        self.cuadro_precio_cita.grid(row=3, column=1, sticky=W)
        self.opciones_estado_cita = ttk.Combobox(self.frame_agendar_cita, state='readonly',
                                                 values=['Atención pendiente', 'Atención confirmada'],
                                                 font=('Times New Roman', 10, 'bold'), width=23)
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

        self.tabla_personal_salud = ttk.Treeview(self.frame_agendar_cita, columns=('DNI', 'Nombres',
                                                                                   'Apellido paterno',
                                                                                   'Apellido materno', 'Teléfono',
                                                                                   'Fecha de nacimiento', 'Dirección',
                                                                                   'Sexo',
                                                                                   'Email', 'Disponibilidad'), height=3)

        self.tabla_personal_salud.column('#0', width=50)
        self.tabla_personal_salud.column('DNI', width=60, anchor=CENTER)
        self.tabla_personal_salud.column('Nombres', width=60, anchor=CENTER)
        self.tabla_personal_salud.column('Apellido paterno', width=80, anchor=CENTER)
        self.tabla_personal_salud.column('Apellido materno', width=80, anchor=CENTER)
        self.tabla_personal_salud.column('Teléfono', width=60, anchor=CENTER)
        self.tabla_personal_salud.column('Fecha de nacimiento', width=120, anchor=CENTER)
        self.tabla_personal_salud.column('Dirección', width=60, anchor=CENTER)
        self.tabla_personal_salud.column('Sexo', width=40, anchor=CENTER)
        self.tabla_personal_salud.column('Email', width=50, anchor=CENTER)
        self.tabla_personal_salud.column('Disponibilidad', width=100, anchor=CENTER)
        self.tabla_personal_salud.config(padding=(5, 10))
        self.tabla_personal_salud.grid(row=6, column=0, columnspan=4, padx=(40, 0))

        self.tabla_personal_salud.heading('#0', text='ID')
        self.tabla_personal_salud.heading('#1', text='DNI')
        self.tabla_personal_salud.heading('#2', text='Nombres')
        self.tabla_personal_salud.heading('#3', text='Apellido paterno')
        self.tabla_personal_salud.heading('#4', text='Apellido materno')
        self.tabla_personal_salud.heading('#5', text='Teléfono')
        self.tabla_personal_salud.heading('#6', text='Fecha de nacimiento')
        self.tabla_personal_salud.heading('#7', text='Dirección')
        self.tabla_personal_salud.heading('#8', text='Sexo')
        self.tabla_personal_salud.heading('#9', text='Email')
        self.tabla_personal_salud.heading('#10', text='Disponibilidad')

        self.scroll_vertical_tabla_personal_salud = Scrollbar(self.frame_agendar_cita,
                                                              command=self.tabla_personal_salud.yview)
        self.scroll_vertical_tabla_personal_salud.grid(row=6, column=4, sticky=NS, padx=(0, 10))
        self.tabla_personal_salud.configure(yscrollcommand=self.scroll_vertical_tabla_personal_salud.set)

    def crear_frame_atender_cita(self):
        if MenuEmssamlud.contador_frame_atender_cita >= 1:
            self.frame_atender_cita.destroy()

        if MenuEmssamlud.contador_frame_inicio >= 1:
            self.frame_opciones_inicio.destroy()

        if MenuEmssamlud.contador_frame_paciente >= 1:
            self.frame_registro_pacientes.destroy()

        if MenuEmssamlud.contador_frame_personal_salud >= 1:
            self.frame_registro_personal_salud.destroy()

        if MenuEmssamlud.contador_frame_agendar_cita >= 1:
            self.frame_agendar_cita.destroy()

        MenuEmssamlud.contador_frame_atender_cita += 1
        self.frame_atender_cita = Frame(self.ventana_principal)
        self.frame_atender_cita.config(bg='#0EB06E', padx=10, pady=20)
        self.frame_atender_cita.grid(row=0, column=3, rowspan=6)

        self.label_id_cita = Label(self.frame_atender_cita, text='ID cita', font=('Times New Roman', 10, 'bold'),
                                   height=3, bg='#0EB06E')
        self.label_id_cita.grid(row=0, column=0, padx=(10, 0), sticky=W)

        self.label_fecha = Label(self.frame_atender_cita, text='Fecha', font=('Times New Roman', 10, 'bold'), height=3,
                                 bg='#0EB06E')
        self.label_fecha.grid(row=1, column=0, padx=(10, 0), sticky=W)

        self.label_sintomas = Label(self.frame_atender_cita, text='Síntomas', font=('Times New Roman', 10, 'bold'),
                                    height=3, bg='#0EB06E')
        self.label_sintomas.grid(row=0, column=2, padx=(10, 0), stick=W)

        self.label_medicamento = Label(self.frame_atender_cita, text='Medicamento',
                                       font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_medicamento.grid(row=4, column=2, padx=(10, 0), stick=W)

        self.label_diagnostico = Label(self.frame_atender_cita, text='Diagnostico',
                                       font=('Times New Roman', 10, 'bold'), height=3, bg='#0EB06E')
        self.label_diagnostico.grid(row=4, column=0, padx=(10, 0), stick=W)

        self.cuadro_id_cita = Entry(self.frame_atender_cita, font=('Times New Roman', 10, 'bold'), width=25)
        self.cuadro_id_cita.grid(row=0, column=1, padx=(10, 0), sticky=W)

        self.cuadro_fecha = DateEntry(self.frame_atender_cita, locale='en_US', date_pattern='mm/dd/y')
        self.cuadro_fecha.grid(row=1, column=1, padx=(10, 0), pady=(0, 20), sticky=W)

        self.cuadro_sintomas = Text(self.frame_atender_cita, font=('Times New Roman', 10, 'bold'), width=20, height=3.5)
        self.cuadro_sintomas.grid(row=0, column=3, padx=(10, 0), sticky=W)

        self.cuadro_medicamentos = Text(self.frame_atender_cita, font=('Times New Roman', 10, 'bold'), width=20,
                                        height=3.5)
        self.cuadro_medicamentos.grid(row=4, column=3, padx=(10, 0), sticky=W)

        self.cuadro_diagnostico = Text(self.frame_atender_cita, font=('Times New Roman', 10, 'bold'), width=20,
                                       height=3.5)
        self.cuadro_diagnostico.grid(row=4, column=1, padx=(10, 0), sticky=W)

        self.frame_botones = Frame(self.frame_atender_cita)
        self.frame_botones.config(bg='#0EB06E', pady=20)
        self.frame_botones.grid(row=5, column=0, columnspan=5, sticky=W)

        self.boton_nuevo = Button(self.frame_botones, text='Nuevo', cursor='hand2')
        self.boton_nuevo.grid(row=0, column=0, padx=(10, 0), sticky=W)

        self.boton_atender = Button(self.frame_botones, text='Atender', cursor='hand2')
        self.boton_atender.grid(row=0, column=1, padx=(70, 0), sticky=W)

        self.boton_modificar = Button(self.frame_botones, text='Modificar', cursor='hand2')
        self.boton_modificar.grid(row=0, column=2, padx=(90, 0), sticky=W)

        self.boton_eliminar = Button(self.frame_botones, text='Eliminar', cursor='hand2')
        self.boton_eliminar.grid(row=0, column=3, padx=(80, 0), sticky=W)

        self.boton_tabla_personal_salud = Button(self.frame_botones, text='Tabla Personal de Salud', cursor='hand2')
        self.boton_tabla_personal_salud.grid(row=1, column=0, padx=(10, 0), pady=(20, 0), sticky=W)

        self.boton_tabla_medicos = Button(self.frame_botones, text='Tabla Médicos', cursor='hand2')
        self.boton_tabla_medicos.grid(row=1, column=1, padx=(70, 0), pady=(20, 0), sticky=W)

        self.boton_tabla_enfermeros = Button(self.frame_botones, text='Tabla Enfermeros', cursor='hand2')
        self.boton_tabla_enfermeros.grid(row=1, column=2, padx=(90, 0), pady=(20, 0), sticky=W)

        self.tabla_atender_cita = ttk.Treeview(self.frame_atender_cita, columns=('ID cita', 'Nombres',
                                                                                 'Apellido paterno', 'Apellido materno',
                                                                                 'Fecha', 'Sintomas', 'Medicamento',
                                                                                 'Diagnostico', 'Email',
                                                                                 'Disponibilidad'), height=3)
        self.tabla_atender_cita.column('#0', width=50)
        self.tabla_atender_cita.column('ID cita', width=60, anchor=CENTER)
        self.tabla_atender_cita.column('Nombres', width=60, anchor=CENTER)
        self.tabla_atender_cita.column('Apellido paterno', width=80, anchor=CENTER)
        self.tabla_atender_cita.column('Apellido materno', width=80, anchor=CENTER)
        self.tabla_atender_cita.column('Fecha', width=60, anchor=CENTER)
        self.tabla_atender_cita.column('Sintomas', width=120, anchor=CENTER)
        self.tabla_atender_cita.column('Medicamento', width=60, anchor=CENTER)
        self.tabla_atender_cita.column('Diagnostico', width=40, anchor=CENTER)
        self.tabla_atender_cita.column('Email', width=50, anchor=CENTER)
        self.tabla_atender_cita.column('Disponibilidad', width=100, anchor=CENTER)
        self.tabla_atender_cita.config(padding=(0, 0))
        self.tabla_atender_cita.grid(row=6, column=0, columnspan=4)

        self.tabla_atender_cita.heading('#0', text='ID')
        self.tabla_atender_cita.heading('ID cita', text='DNI')
        self.tabla_atender_cita.heading('Nombres', text='Nombres')
        self.tabla_atender_cita.heading('Apellido paterno', text='Apellido paterno')
        self.tabla_atender_cita.heading('Apellido materno', text='Apellido materno')
        self.tabla_atender_cita.heading('Fecha', text='Fecha')
        self.tabla_atender_cita.heading('Sintomas', text='Sintomas')
        self.tabla_atender_cita.heading('Medicamento', text='Medicamento')
        self.tabla_atender_cita.heading('Diagnostico', text='Diagnostico')
        self.tabla_atender_cita.heading('Email', text='Email')
        self.tabla_atender_cita.heading('Disponibilidad', text='Disponibilidad')

        self.scroll_vertical_tabla_atender_cita = Scrollbar(self.frame_atender_cita,
                                                            command=self.tabla_atender_cita.yview)
        self.scroll_vertical_tabla_atender_cita.grid(row=6, column=4, sticky=NS, padx=(0, 10))
        self.tabla_atender_cita.configure(yscrollcommand=self.scroll_vertical_tabla_atender_cita.set)

    def disenno_interfaz_menu_principal(self):
        self.ventana_principal = Frame(self)
        self.ventana_principal.config(bg='#9DE8E2')
        self.ventana_principal.pack(fill=BOTH, expand=True, pady=40)

        self.titulo_ventana = Label(self, text='Sistema de citas médicas - Emsamlud', bg='#0EB06E',
                                    font=('Times New Roman', 18, 'bold'), padx=100)
        self.titulo_ventana.place(x=330, y=4)

        self.logo_admin = PhotoImage(file='imagenes/logo_admin.png')
        self.cuadro_logo_admin = Label(self.ventana_principal, image=self.logo_admin, bg='#9DE8E2')
        self.cuadro_logo_admin.grid(row=0, column=0, columnspan=2, padx=(33, 0), sticky=S)
        self.cuadro_admin = Label(self.ventana_principal, text='Administrador', bg='#9DE8E2', fg='#117E5E',
                                  font=('Times New Roman', 18, 'bold'))
        self.cuadro_admin.grid(row=1, column=0, columnspan=2, padx=(30, 0), sticky=N)
        self.separador_horizontal = Frame(self.ventana_principal)
        self.separador_horizontal.config(bg='#0EB06E', height=12, width=228)
        self.separador_horizontal.place(x=0, y=217)
        self.ventana_inicio()

    def menu_opciones(self):
        self.imagen_opcion_inicio = PhotoImage(file="imagenes/logo_inicio.png")

        self.boton_inicio = Button(self.ventana_principal, image=self.imagen_opcion_inicio, command=self.ventana_inicio,
                                   cursor='hand2', height=38, width=98)
        self.boton_inicio.grid(row=2, column=0, columnspan=2, padx=(35, 0), sticky=N)

        self.imagen_opcion_agendar_cita = PhotoImage(file="imagenes/logo_agendar_cita.png")
        self.boton_agendar_cita = Button(self.ventana_principal, image=self.imagen_opcion_agendar_cita,
                                         command=self.crear_frame_agendar_cita, cursor='hand2', height=38, width=98)
        self.boton_agendar_cita.grid(row=3, column=0, columnspan=2, padx=(35, 0), sticky=N)

        self.imagen_opcion_atender_cita = PhotoImage(file="imagenes/logo_atender_cita.png")
        self.boton_atender_cita = Button(self.ventana_principal, image=self.imagen_opcion_atender_cita,
                                         command=self.crear_frame_atender_cita, cursor='hand2', height=38, width=98)
        self.boton_atender_cita.grid(row=4, column=0, columnspan=2, padx=(35, 0), sticky=N)

        self.imagen_opcion_reportes = PhotoImage(file="imagenes/logo_reportes.png")
        self.boton_reportes = Button(self.ventana_principal, image=self.imagen_opcion_reportes, cursor='hand2',
                                     height=38, width=98)
        self.boton_reportes.grid(row=5, column=0, columnspan=2, padx=(35, 0), sticky=N)

        self.separador_vertical = Label(self.ventana_principal)
        self.separador_vertical.config(bg='#0EB06E', height=35, width=1)
        self.separador_vertical.grid(row=0, column=2, rowspan=6, padx=40)