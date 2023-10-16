
from helpers.helper import line
from options_func.options_func import OptionFunc

from config.menu import MENU_OPTIONS, SUB_RENDERIZAR

class MenuOption:
    def __init__(self):
        self.state = False
        self.options = MENU_OPTIONS
        self.sub_option = SUB_RENDERIZAR

    def startWindow(self):
        line()
        print("Inicando software de Imagen")

        state = False

        while state == False:

            self.showMenu()
            option = self.getKey()

            option_func = OptionFunc(option)
            select = option_func.eject_function()

            state = select

            # if option != False:
            #     self.line()
            #     # self.clean()
            #     print(f"opcion seleccionada {option}")         
            #     # state = True
            # if option == False:
            #     self.clean()
            #     self.line()
            #     print("opcion no existe o mal seleccionada")
            #     print("Intente nuevamente")

            line()


    def showMenu(self):
        count = 1
        for i in self.options:
            title = self.options[count]
            print(f"{count} - {title}")
            count += 1


    def getKey(self):
        option = str(input("selecciona una opcion \n"))
        try:
            select = int(option)
            return select
        except:
            return False




