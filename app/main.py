from options_func.render_image import RenderImage
from window.main_window import *
from window.menu_option import MenuOption


def main():
    # ? esta eslel incio del software general
    # start = MenuOption()
    # start.startWindow()

    start = RenderImage()
    start.get_img_folder()


if __name__ == "__main__":
    main()