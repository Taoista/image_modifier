import os

class MenuOption:
    def __init__(self):
        self.state = False
        self.options = {
                1: "Renderizar Imagenes",
                2: "Voletar ->",
                3: "Voltear V"
            }

    def startWindow(self):
        self.clean()
        self.line()
        print("Inicando software de Imagen")
        
        for i in self.options:
            print(i)

        self.getKey()
        self.line()
        pass


    def showMenu(self, option):
        select = int(option)
        try:
            return self.options[select]
        except:
            return False
    


    def getKey(self):
        option = str(input("selecciona una opcion \n"))

        selected = self.showMenu(option)

        print(selected)


    def line(self):
        print("--------------------------------------")

    def clean(self):
        os.system('cls' if os.name == 'nt' else 'clear')