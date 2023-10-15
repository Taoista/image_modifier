from tkinter import *
from tkinter import filedialog
from tkinter import ttk

class MainWindow:
    def __init__(self, width, heght, title):
        self.width = width
        self.heght = heght
        self.title = title
        self.folder_start = None
        self.folder_end = None


    def init_window(self):

        root = Tk()
        root.title("Frames")

        buscador = LabelFrame(root, text="Buscador", padx=100, pady=100)
        buscador.grid(row=0, column=0, padx=100, pady=100)

        barra = Entry(buscador, text="¿Buscas algo?").pack()
        boton = Button(buscador, text="Buscar").pack()

        mainloop()


    def init_window2(self):
        tk = Tk()
        tk.geometry(f"{self.width}x{self.heght}")  # Ancho x Alto en píxeles
        tk.title(f"{self.title}")

        label_frame = LabelFrame(tk, text="Datos Personales")
        label_frame.grid(column=0, row=0, padx=20, pady=20)

    # Agregar widgets al LabelFrame
        etiqueta_nombre = Label(label_frame, text="Nombre:")
        etiqueta_nombre.grid(column=1, row=0, ipadx=10, ipady=10)
        etiqueta_nombre = Label(label_frame, text="Nombre:")
        etiqueta_nombre.grid(column=2, row=0, ipadx=10, ipady=10)

        # ? boton selector de imagen
        #Button(tk, text="Origen", command=self.select_images_origin).place(x="10",y="10")
        # ? boton sleectr de temrino de las imagenes
        #Button(tk, text="Termino", command=self.select_images_end).place(x="120",y="10")
        

        tk.mainloop()
            

    def select_images_origin(self):
        folder_select = filedialog.askdirectory()
        if folder_select:
            self.folder_start = folder_select

    def select_images_end(self):
        pass

#
# en volumen
# seleccion de archivo entrada y salida
#
#
# seleccionar origen y termino
# renderiazar imagen
# voltear imagen
# optimizar imagen
# cambiar formato de la image
# 