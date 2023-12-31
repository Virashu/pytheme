import os
import pyautogui
import sys
import subprocess


if len(sys.argv) < 2:
    print("usage:    pt <theme>\nuse 'pt themes' to get all available themes")
    quit()

theme = sys.argv[1]

themes = {
    "red": {
        "wallpaper": "~/Pictures/godishs-hires.jpg",
        "color": "color9",
    },
    "red2": {
        "wallpaper": "~/Pictures/godishb-hires.jpg",
        "color": "color9",
    },
    "green": {
        "wallpaper": "~/Pictures/green\\ leaves.jpg",
        "color": "color10",
    },
    "greenbug": {
        "wallpaper": "~/Pictures/bug.jpg",
        "color": "color10",
    },
    "blue": {
        "wallpaper": "~/Pictures/meat.jpg",
        "color": "color12",
    },
    "pink": {
        "wallpaper": "~/Pictures/happy\\ lucky.jpg",
        "color": "color13",
    },
    "pinks": {
        "wallpaper": "~/Pictures/shinobu4.jpg",
        "color": "bg4",
    },
    "blackpink": {
        "wallpaper": "~/Pictures/лэйн.png",
        "color": "color13",
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
    color = themes[theme]['color']
    newcolor = subprocess.getoutput("xrdb -query | grep -Po '(?<=\\*.%s:\\t)(#[0-9abcdef]{6})'" % (color))
    os.system("echo %s >> log.txt" % (newcolor))
    for l in res:
        if l.startswith("dwm.selbgcolor:"):
            # r.append('!' + l)
            r.append("dwm.selbgcolor: {}\n".format(newcolor))
        elif l.startswith("dwm.selbordercolor:"):
            #r.append("dwm.selbordercolor: {}\n".format(themes[theme]['color']))
            r.append("dwm.selbordercolor: {}\n".format(newcolor))

        else:
            r.append(l)

with open("/home/virashu/.Xresources", "w+") as f:
    f.write(''.join(r))

os.system("xrdb -merge /home/virashu/.Xresources")
pyautogui.hotkey("win", "shift", "r")
