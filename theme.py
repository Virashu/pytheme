import os
import pyautogui
import sys


if len(sys.argv) < 2:
    print("usage:    pt <theme>\nuse 'pt themes' to get all available themes")
    quit()

theme = sys.argv[1]

themes = {
    "red": {
        "wallpaper": "~/Pictures/godishs-hires.jpg",
        "color": "#fb4934",
    },
    "green": {
        "wallpaper": "~/Pictures/green\\ leaves.jpg",
        "color": "#b8bb26",
    },
    "greenbug": {
        "wallpaper": "~/Pictures/bug.jpg",
        "color": "#b8bb26",
    },
    "blue": {
        "wallpaper": "~/Pictures/meat.jpg",
        "color": "#83a598",
    },
    "pink": {
        "wallpaper": "~/Pictures/_125701737_kuromi.jpg",
        "color": "#d3869b",
    },
    "pinks": {
        "wallpaper": "~/Pictures/shinobu4.jpg",
        "color": "#d3869b",
    },
    "blackpink": {
        "wallpaper": "~/Pictures/лэйн.png",
        "color": "#d3869b",
    },
}

if theme == "themes":
    print("List of available themes:")
    for theme in themes.keys():
        print(" -", theme)
    quit()

if theme not in themes:
    print("theme not found")
    quit()

os.system("feh --bg-fill {}".format(themes[theme]['wallpaper']))

with open("/home/virashu/.Xresources", "r+") as f:
    res = f.readlines()
    r = []
    for l in res:
        if l.startswith("dwm.selbgcolor:"):
            # r.append('!' + l)
            r.append("dwm.selbgcolor: {}\n".format(themes[theme]['color']))
        elif l.startswith("dwm.selbordercolor:"):
            r.append("dwm.selbordercolor: {}\n".format(themes[theme]['color']))
        else:
            r.append(l)

with open("/home/virashu/.Xresources", "w+") as f:
    f.write(''.join(r))

os.system("xrdb -merge /home/virashu/.Xresources")
pyautogui.hotkey("win", "shift", "r")
