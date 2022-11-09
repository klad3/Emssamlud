from tkinter import *
import util.centrar_ventana as utl
#prueba
class MenuEmsamlud(Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry('1200x600')
        utl.centrar_ventana(self, 1200, 600)
        self.title('Emsamlud - Sistema')
        self.config(bg='#0EB06E')
        self.resizable(False, False)
        self.disenno_interfaz_menu_principal()
        self.menu_opciones()

    def disenno_interfaz_menu_principal(self):
        self.ventana_principal = Frame(self)
        self.ventana_principal.config(bg='#9DE8E2')
        self.ventana_principal.pack(fill=BOTH, expand=True, pady=40)

        self.titulo_ventana = Label(self, text='Sistema de citas médicas - Emssamlud', bg='#0EB06E' ,font=('Times New Roman', 18, 'bold'), padx=100)
        self.titulo_ventana.place(x=330, y=4)

        self.logo_admin = PhotoImage(file='imagenes/logo_admin.png')
        self.cuadro_logo_admin = Label(self.ventana_principal, image=self.logo_admin, bg='#9DE8E2')
        self.cuadro_logo_admin.grid(row=0, column=0, columnspan=2, padx=(33, 0), sticky=S)
        self.cuadro_admin = Label(self.ventana_principal, text='Administrador', bg='#9DE8E2', fg='#117E5E', font=('Times New Roman', 18, 'bold'))
        self.cuadro_admin.grid(row=1, column=0, columnspan=2, padx=(30, 0), sticky=N)
        self.separador_horizontal = Frame(self.ventana_principal)
        self.separador_horizontal.config(bg='#0EB06E', height=12, width=228)
        self.separador_horizontal.place(x=0, y=230)

    def menu_opciones(self):
        self.boton_inicio = Button(self.ventana_principal, text='Inicio', cursor='hand2')
        self.boton_inicio.grid(row=2, column=0, columnspan=2, padx=(35, 0), pady=(10, 0), sticky=N, ipadx=30)

        self.boton_agendar_cita = Button(self.ventana_principal, text='Agendar cita', cursor='hand2')
        self.boton_agendar_cita.grid(row=3, column=0, columnspan=2, padx=(35, 0), sticky=N, ipadx=30)

        self.boton_atender_cita = Button(self.ventana_principal, text='Atender cita', cursor='hand2')
        self.boton_atender_cita.grid(row=4, column=0, columnspan=2, padx=(35, 0), sticky=N, ipadx=30)

        self.boton_reportes = Button(self.ventana_principal, text='Reportes', cursor='hand2')
        self.boton_reportes.grid(row=5, column=0, columnspan=2, padx=(35, 0), sticky=N, ipadx=30)

        self.separador_vertical = Label(self.ventana_principal)
        self.separador_vertical.config(bg='#0EB06E', height=35, width=1)
        self.separador_vertical.grid(row=0, column=2, rowspan=6, padx=40)