# 
# ! sin terminar no ejectuar
# 
from setuptools import setup, find_packages

setup(
    name='mi_proyecto',
    version='1.0.0',
    description='Descripción de mi proyecto',
    author='Tu Nombre',
    author_email='tu@email.com',
    url='https://github.com/tu_usuario/tu_proyecto',
    packages=find_packages(),
    install_requires=[
        # Lista de dependencias requeridas
        'requests',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'mi_comando=mi_proyecto.main:main_function',
        ],
    },
)
