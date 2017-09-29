#! /usr/bin/env python
# todo: 
#	change the tkinter import not to use *
#	clean up the code
#	decide whether to close the gui after making the selection and pasting the text

import pyautogui
import os
from tkinter import *

# setting up the templates directory and obtaining a list of the files in it
destdir = '/home/dantata/python/template101/templates/'
files = [ f for f in os.listdir(destdir) if os.path.isfile(os.path.join(destdir,f)) ]

master = Tk()

# geting the selection from the optionsmenu and pasting the text into the active window
def paste_selection(value):
    #print(destdir + value)
    f = open(destdir + value, 'r')
    file_contents = f.read()

    pyautogui.hotkey('alt','tab')
    pyautogui.typewrite(file_contents)

    f.close()
    #sys.exit()


variable = StringVar(master)
variable.set("Click me!") # default value

w = OptionMenu(master, variable, *files,command=paste_selection)
w.pack()


mainloop()
