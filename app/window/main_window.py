import eel

class MainWindow:
    def __init__(self):
        pass

    def init_window(self):
        eel.init('web', allowed_extensions=['.js', '.html'])
        eel.start("index.html", size=(1366, 743), port=8001)

    def select_images_origin(self):
        # folder_select = filedialog.askdirectory()
        # if folder_select:
        #     self.folder_start = folder_select
        pass


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