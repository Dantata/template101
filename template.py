#! /usr/bin/env python

# todo: 
#	change the tkinter import not to use *
#	clean up the code
#	decide whether to close the gui after making the selection and pasting the text

import pyautogui
import os
from tkinter import *
import pyperclip

# setting up the templates directory and obtaining a list of the files in it
destdir = 'templates/'
files = [ f for f in os.listdir(destdir) if os.path.isfile(os.path.join(destdir,f)) ]

master = Tk()

# geting the selection from the optionsmenu and pasting the text into the active window
def paste_selection(value):
    #print(destdir + value)
    f = open(destdir + value, 'r')
    file_contents = f.read()

    #pyautogui.click(100, 100); pyautogui.typewrite(file_contents)
    pyperclip.copy(file_contents)

    #print (file_contents)
    f.close()


variable = StringVar(master)
variable.set("Click me!") # default value

w = OptionMenu(master, variable, *files,command=paste_selection)
w.pack()

mainloop()