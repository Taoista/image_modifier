from PIL import Image
import os

from config.menu import FOLDER_ORIGIN, FOLDER_FINISH, IMG_EXTENCION


class ZoomImage:
    def __init__(self, percent_zoom):
        self.folder_origin = FOLDER_ORIGIN
        self.c_drive_path = "C:\\"
        self.folder_finish = FOLDER_FINISH
        self.percent_zoom = percent_zoom
        self.image_extensions = IMG_EXTENCION

    def start_zoom(self):
        print("Iniciando el renderizado de la imagen")
        origin_folder_path = os.listdir(self.c_drive_path+self.folder_origin)
        

        for file_image in origin_folder_path:
            # path_image = os.path.join(self.c_drive_path,name)
            name, ext = os.path.splitext(file_image)
            self.generate_zoom(file_image, ext, name)

         


    def generate_zoom(self, file_image, extencion, name):
        imagen = Image.open(f"{self.c_drive_path}{self.folder_origin}\\{file_image}")
        width, height = imagen.size
        medida_width = int(width * float("0."+str(self.percent_zoom)))
        medida_height = int(height * float("0."+str(self.percent_zoom)))

        # Especifica la región que deseas "zoom" utilizando coordenadas de píxeles
        region = (0, 0, medida_width, medida_height)
        # Recortar la región especificada de la imagen original
        imagen_recortada = imagen.crop(region)

        # Redimensionar la imagen recortada para que parezca un zoom
        nuevo_tamano = imagen.size  # Mismo tamaño que la imagen original
        imagen_zoom = imagen_recortada.resize(nuevo_tamano)

        # Crear un lienzo blanco del mismo tamaño que la imagen original
        lienzo = Image.new("RGB", imagen.size, (255, 255, 255))

        # Pegar la imagen con zoom en el centro del lienzo
        posicion = ((imagen.width - imagen_zoom.width) // 2, (imagen.height - imagen_zoom.height) // 2)
        lienzo.paste(imagen_zoom, posicion)

        # Guardar la imagen file_image
        # lienzo.save(f"{self.c_drive_path}{self.folder_finish}\\{ file_image }")
        lienzo.save(f"{self.c_drive_path}{self.folder_finish}\\{ name }-1{extencion}")
        # lienzo.show()
