import os

from config.menu import MENU_OPTIONS


class OptionFunc:
    def __init__(self, select):
        self.options = MENU_OPTIONS
        self.select = select
    
    def eject_function(self):
        # ? renderiza la imagen
        if self.options[self.select] == 1:
            return False
        # ? voleta la imagen hacia la derecha
        if self.options[self.select] == 2:
            return False
        # ? voleta la imagen hacia abajo
        if self.options[self.select] == 3:
            return False
        # ? sale del software
        if self.options[self.select] == 4:
            return self.close_software()

        self.close_software()

    def close_software(self):
        os.system('exit')
