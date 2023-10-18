import os
from options_func.zoom_image import ZoomImage

from helpers.helper import line

from config.menu import MENU_OPTIONS


class OptionFunc:
    def __init__(self, select):
        self.options = MENU_OPTIONS
        self.select = select
    


    def eject_function(self):
        # ? renderiza la imagen
        line()
        if self.select == 1:
            print(f"ejencutando la funcion {self.select}")
            return False
        # ? voleta la imagen hacia la derecha
        if self.select == 2:
            print(f"ejencutando la funcion {self.select}")
            return False
        # ? voleta la imagen hacia abajo
        if self.select == 3:
            print(f"ejencutando la funcion {self.select}")
            return False
        # ? modificar zoom
        if self.select == 4:
            number = input("Cuanto zoom le quieres dar %\n")
            try:
                percent_zoom = int(number)
                zoom = ZoomImage(percent_zoom)
                zoom.start_zoom()
            except ValueError:
                print("No es un número")
           
            return False
        # ? sale del software
        if self.select == 5:
            print(f"ejencutando la funcion {self.select} .. Saliendo")
            return True
        

        print("opcion no existe, intente nuevamente")

        return True

    def close_software(self):
        os.system('exit')


    def showSubInfo(self):
        pass