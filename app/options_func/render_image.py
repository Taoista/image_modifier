import os
from PIL import Image
import pandas as pd

from config.menu import IMG_EXTENCION


class RenderImage:
    def __init__(self):
        # ? iniciando el registro de la imagen si no existe
        self.origin_folder_name = "img_modifier_origen"
        self.final_folder_name = "img_modifier_final"
        self.c_drive_path = "C:\\"
        self.image_extensions = IMG_EXTENCION

        self.set_folders()


    def get_img_folder(self):
        origin_folder_path = os.path.join(self.c_drive_path, self.origin_folder_name)
        file_list = os.listdir(origin_folder_path)

        elements = list()

        for image in file_list:
            file_path = os.path.join(origin_folder_path, image)
            if os.path.isfile(file_path):
                name, extension = os.path.splitext(image)
                # ? verificar extencion
                for ext in self.image_extensions:
                    if ext == extension:
                        full_name = name+'-1'+extension
                        elements.append({"name": name, "file_path": file_path})
                        # print(name, extension, file_path),
                        self.forma_mirrow(file_path,full_name)

        # ? exporta a excel
        self.export_excel(elements)


    # * trasnforma la imagen tipo espejos
    def forma_mirrow(self, path_image, name_image):
        image = Image.open(path_image)
        finaL_PATH = os.path.join(self.c_drive_path, self.final_folder_name)
        iamge_mirror = image.transpose(Image.FLIP_LEFT_RIGHT)
        iamge_mirror.save(finaL_PATH+'\\'+name_image)
        image.close()
        iamge_mirror.close()

    # * crea los directorios
    def set_folders(self):
        # Ruta a la raíz de la unidad C:
        c_drive_path = self.c_drive_path
        
        # Nombres de las carpetas que deseas crear
        origin_folder_name = self.origin_folder_name
        final_folder_name = self.final_folder_name
        
        origin_folder_path = os.path.join(c_drive_path, origin_folder_name)
        final_folder_path = os.path.join(c_drive_path, final_folder_name)

        # Verificar si las carpetas existen, si no, crearlas
        if not os.path.exists(origin_folder_path):
            os.mkdir(origin_folder_path)
            print(f'Se ha creado la carpeta "{origin_folder_name}" en la raíz de la unidad C.')

        if not os.path.exists(final_folder_path):
            os.mkdir(final_folder_path)
            print(f'Se ha creado la carpeta "{final_folder_name}" en la raíz de la unidad C.')
        
        return True
    
    # * solo uso demo exporta en excel
    def export_excel(self, array):
        df = pd.DataFrame(array)

        # Ruta y nombre del archivo Excel
        excel_file =  finaL_PATH = os.path.join(self.c_drive_path, self.final_folder_name)+"\\datos.xlsx"

        # Exportar el DataFrame a un archivo Excel
        df.to_excel(excel_file, index=False)