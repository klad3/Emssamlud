from tkinter import *
from tkinter.font import BOLD
import clases.admin as adm
import menu_principal
import util.centrar_ventana as pv

class Login(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry('450x600')
        pv.centrar_ventana(self, 450, 600)
        self.title('Emsamlud - Inicio de sesión')
        self.logo_ventana = PhotoImage(file='imagenes/logo_ventana.png')
        self.wm_iconphoto(True, self.logo_ventana)
        self.config(bg='#0EB06E', padx=20, pady=20)
        self.resizable(False, False)
        self.disenno_interfaz_login()

    def ingresar_sistema(self):
        admin = adm.Admin()
        admin.login(self.usuario.get(), self.password.get())

        if admin.accede_sistema:
            self.withdraw()
            self.ventana_principal = menu_principal.MenuEmssamlud()
            self.ventana_principal.protocol("WM_DELETE_WINDOW",self.destroy)

    def disenno_interfaz_login(self):
        self.cuadro_imagen = Frame(self)
        self.cuadro_imagen.pack(pady=(0, 20))

        self.logo_emsamlud = PhotoImage(file='imagenes/logo_emsamlud.PNG')

        Label(self.cuadro_imagen, image=self.logo_emsamlud, bg='#0EB06E').pack()

        self.cuadro_titulo_login = Frame(self)
        self.cuadro_titulo_login.config(bg='#9DE8E2', pady=20)
        self.cuadro_titulo_login.pack(fill=BOTH, expand=True)

        Label(self.cuadro_titulo_login, text='ACCESO', font=('Times New Roman', 18, BOLD), bg='#9DE8E2', fg='#0EB06E').pack()

        self.frame_usuario_password = Frame(self.cuadro_titulo_login)
        self.frame_usuario_password.config(bg='#9DE8E2', pady=20)
        self.frame_usuario_password.pack()

        self.linea_cuadro_usuario = Frame(self.frame_usuario_password)
        self.linea_cuadro_usuario.config(bg='#0EB06E', height=70, width=242)
        self.linea_cuadro_usuario.place(x=26, y=0)

        self.cuadro_usuario = Frame(self.frame_usuario_password)
        self.cuadro_usuario.config(bg='#9DE8E2')
        self.cuadro_usuario.pack(pady=(0, 20))

        self.logo_usuario = PhotoImage(file='imagenes/logo_usuario.png')
        Label(self.cuadro_usuario, image=self.logo_usuario, bg='#9DE8E2').grid(row=0, column=0)

        self.usuario = StringVar()
        self.cuadro_usuario = Entry(self.cuadro_usuario, bg='#9DE8E2', fg='#0EB06E', font=18, highlightthickness=1, highlightbackground='#9DE8E2', highlightcolor='#9DE8E2', textvariable=self.usuario, width=20)

        self.cuadro_usuario.grid(row=0, column=1, sticky=S, padx=(0, 10))

        self.linea_cuadro_password = Frame(self.frame_usuario_password)
        self.linea_cuadro_password.config(bg='#0EB06E', height=58, width=242)
        self.linea_cuadro_password.place(x=28, y=99)

        self.frame_password = Frame(self.frame_usuario_password)
        self.frame_password.config(bg='#9DE8E2')
        self.frame_password.pack(pady=(0, 20), padx=(9, 0))

        self.logo_password = PhotoImage(file='imagenes/logo_password.png')      

        Label(self.frame_password, image=self.logo_password, bg='#9DE8E2').grid(row=0, column=0, padx=(20, 0))

        self.password = StringVar()
        self.cuadro_password = Entry(self.frame_password, bg='#9DE8E2', fg='#0EB06E', font=18, show='•', textvariable=self.password)
        self.cuadro_password.grid(row=0, column=1, sticky=S)

        self.contador_mostrar_password = 0
        def mostrar_password():
            self.contador_mostrar_password += 1
            if self.contador_mostrar_password % 2 != 0:
                self.cuadro_password.config(show='')
                self.boton_mostrar_password.config(image=self.imagen_ocultar_password)
            else:
                self.cuadro_password.config(show='•')
                self.boton_mostrar_password.config(image=self.imagen_mostrar_password)
                
        self.imagen_mostrar_password = PhotoImage(file='imagenes/logo_mostrar_password.png')
        self.imagen_ocultar_password = PhotoImage(file='imagenes/logo_ocultar_password.png')

        self.boton_mostrar_password = Button(self.frame_password, image=self.imagen_mostrar_password, command=mostrar_password, bg='#9DE8E2')
        self.boton_mostrar_password.grid(row=0, column=2, sticky=SE, padx=(10, 0))

        self.cuadro_boton = Frame(self.frame_usuario_password)
        self.cuadro_boton.config(bg='#9DE8E2')
        self.cuadro_boton.pack()

        self.boton_ingresar = Button(self.cuadro_boton, text='Ingresar', bg='#9DE8E2', command=self.ingresar_sistema, cursor='hand2')
        self.boton_ingresar.bind('<Enter>', lambda e: e.widget.config(bg='#0EB06E'))
        self.boton_ingresar.bind('<Leave>', lambda e: e.widget.config(bg='#9DE8E2'))
        self.boton_ingresar.grid(row=0, column=0, columnspan=2, ipadx=59)

if __name__=='__main__':
    raiz = Login()
    raiz.mainloop()