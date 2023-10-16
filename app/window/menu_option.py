import os

from config.menu import MENU_OPTIONS

class MenuOption:
    def __init__(self):
        self.state = False
        self.options = MENU_OPTIONS

    def startWindow(self):
        self.clean()
        self.line()
        print("Inicando software de Imagen")

        state = False

        while state == False:
            self.showMenu()
            option = self.getKey()

            if option != False:
                self.line()
                self.clean()
                print(f"opcion seleccionada {option}")         
                state = True
            if option == False:
                self.clean()
                self.line()
                print("opcion no existe o mal seleccionada")
                print("Intente nuevamente")

            self.line()


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
            return self.options[select]
        except:
            return False



    def line(self):
        print("--------------------------------------")

    def clean(self):
        os.system('cls' if os.name == 'nt' else 'clear')