import os
import sys
import pyautogui
import subprocess


def main():
    dir = os.path.dirname(os.path.abspath(__file__))

    themes = map(lambda a: a.replace('.xres', ''), os.listdir(f"{dir}{os.sep}themes"))


    if len(sys.argv) < 2:
        print("Available themes: ")
        for theme in themes:
            if theme == 'general' or theme == 'template':
                continue
            print(" - ", theme)
        return
    theme = sys.argv[1]
    if theme not in themes:
        print("Theme not found")
        return
    os.system(f"xrdb -merge {dir}{os.sep}themes{os.sep}template.xres")
    os.system("xrdb -merge /home/virashu/.Xresources")
    os.system("xrdb -merge {}".format(f"{dir}{os.sep}themes{os.sep}{theme}.xres"))
    os.system(f"xrdb -merge {dir}{os.sep}themes{os.sep}general.xres")
    with open("/home/virashu/.Xresources", "w") as f:
        f.write(subprocess.getoutput("xrdb -query"))
    with open("/home/virashu/.config/kitty/colors.conf", "w") as f:
        f.write(subprocess.getoutput("xrdb -query | python /home/virashu/scripts/xres_to_kitty.py"))
        
    with open(f"{dir}{os.sep}themes{os.sep}{theme}.xres", "r") as f:
        for line in f.readlines():
            if line.startswith("wallpaper:"):
                wallpaper = line.split()[-1]
                os.system("feh --bg-fill {}".format(wallpaper))
    pyautogui.hotkey("win", "shift", "r")

if __name__ == '__main__':
    main()
