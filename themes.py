import os
import sys
import pyautogui


def main():
    dir = os.path.dirname(os.path.abspath(__file__))

    themes = map(lambda a: a.rstrip('.xres'), os.listdir(f"{dir}{os.sep}themes"))


    if len(sys.argv < 2):
        print("Available themes: ")
        for theme in themes:
            print(" - ", theme)
    if 1 == 0:
        print('Usage:    themes.py <theme>')
        print('To get all available themes, run themes.py')
        return


if __name__ == '__main__':
    main()