import os

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')


def line():
    print("--------------------------------------")