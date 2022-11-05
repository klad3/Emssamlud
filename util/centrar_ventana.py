from PIL import ImageTk, Image

def centrar_ventana(self,aplicacion_ancho,aplicacion_largo):
    pantall_ancho = self.winfo_screenwidth()
    pantall_largo = self.winfo_screenheight()
    x = int((pantall_ancho/2) - (aplicacion_ancho/2))
    y = int((pantall_largo/2) - (aplicacion_largo/2))
    return self.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")