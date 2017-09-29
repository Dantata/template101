#! /usr/bin/env python
# todo: 
#	change the tkinter import not to use *
#	clean up the code
# 	somehow make a nested optionmenu in order to implement /abuse templates from separate directory

import pyautogui
import os
from tkinter import *

# setting up the templates directory and obtaining a list of the files in it
destdir = '/home/dantata/python/template101/template101/templates/'

files = [ f for f in os.listdir(destdir) if os.path.isfile(os.path.join(destdir,f)) ]

master = Tk()

# geting the selection from the optionsmenu and pasting the text into the active window
def paste_selection(value):
    
    f = open(destdir + value, 'r')
    file_contents = f.read()

	# ALT+TAB in order to return to textarea and then paste the text from the template txt file
    pyautogui.hotkey('alt','tab')
    pyautogui.typewrite(file_contents)

    f.close()
    sys.exit()


variable = StringVar(master)
variable.set("Click me!") # default value

w = OptionMenu(master, variable, *files,command=paste_selection)
w.pack()

mainloop()
