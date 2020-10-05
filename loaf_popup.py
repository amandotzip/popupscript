#!/usr/bin/env python
import tkinter as tk
from PIL import Image, ImageTk
import random
#https://stackoverflow.com/questions/34023604/open-tkinter-multiple-windows-with-delay-python

root = tk.Tk()
tk.Label(root, text="this is the root window").pack()
root.geometry("10x10")
l = []

popUpAmount = 1000
# recursive function for efficient one line use of var i, simply reduces code
def showPic(i):
    if(i<popUpAmount):
        loc = "./almighty_loaf.jpg"
        img = Image.open(loc)
        img.load()
        photoImg = ImageTk.PhotoImage(img)
        l.append(photoImg)

        window = tk.Toplevel()
        # random coordinates of popup window
        xCoord = random.randint(-200,1200)
        yCoord = random.randint(-200,300)
        winPosition = "+{}+{}".format(xCoord, yCoord)#insert coordinates into string
        window.geometry(winPosition)
        tk.Label(window, image=photoImg).pack()# opens image in gui
        root.after(50, lambda:showPic(i+1))#first param is miliseconds to open
    #   root.after(1000-i*100, lambda:showPic(i+1))#makes speed of pop up increase over time
    #   (replaces line above)
    else:
        return

root.after(0, showPic(1))
root.mainloop()
