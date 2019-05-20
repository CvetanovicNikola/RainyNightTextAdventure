
from tkinter import *
from PIL import ImageTk
import PIL.Image
import whGame
import time
from io import StringIO
import os
import sys


def play():

    window.destroy()
    whGame.start_screen()


def help():
    content = """\nWelcome to the Rainiy night,
        this is a textual adventure game
        set in the world of Warhammer fantasy.
        Your character is a thief returning from
        a mission and needs to deliver the 
        loot to the employers.
        She or he needs to be quick, the employers
        requested the loot to brought in a short
        time period.

        The scenario is lossly based on an
        tabletop adventure played by Radoš,
        Rastko and Nik. 
        Techincal advice by Mrki.

        How to play :
        you will be presented by a description
        of a location and situation your 
        character is in read carefully 
        and type your input + enter,
        usally your input will be in form of 
        numbered choices but sometimes 
        you can enter commands that are not 
        on the menu.
        
        Type 'inventory' to view your inventory
        or 'q' to quit
        You can always type 'help' for help

        Use your imagination and have fun! """
    display.delete("1.0", END)
    display.insert(INSERT, content)


def quit():
    content = """You leave your fate in Sigmar's hands. 
                Auf wiederzhn!"""
    display.delete("1.0", END)
    display.insert(INSERT, content)
    window.update_idletasks()
    time.sleep(5)
    window.update_idletasks()
    sys.exit(1)


window = Tk()
window.geometry("600x620")
window.resizable(0, 0)
window.configure(background="gray")
window.title("A rainy night in old world")

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
pilImage = PIL.Image.open(
    os.path.join(dirname, "back.png"))
pilImage = pilImage.resize((400, 400))

img = ImageTk.PhotoImage(pilImage)

img_label = Label(image=img)
img_label.image = img
img_label.configure(background="gray")
img_label.grid(row=0, column=2, columnspan=6,
               rowspan=6, padx=100, pady=(10, 10))

label_play = Label(window, text="Play")
label_play.configure(background="gray")
label_play.grid(row=0, column=1, padx=(30, 0), pady=10)

label_help = Label(window, text="Help")
label_help.configure(background="gray")
label_help.grid(row=1, column=1, padx=(30, 0), pady=10)

label_quit = Label(window, text="Quit")
label_quit.configure(background="gray")
label_quit.grid(row=2, column=1, padx=(30, 0), pady=10)


pilImage_start = PIL.Image.open(
    os.path.join(dirname, "icon_start.png"))
pilImage_start = pilImage_start.resize((50, 70))

img_start = ImageTk.PhotoImage(pilImage_start)

button_play = Button(window, text="Play", image=img_start,
                     width=50, height=40, command=play)
button_play.config(relief="raised")
button_play.configure(background="gray")
button_play.grid(row=0, column=2, padx=(0, 15), pady=10)


button_help = Button(window, text="Help", image=img_start,
                     width=50, height=40, command=help)
button_help.config(relief="raised")
button_help.configure(background="gray")
button_help.grid(row=1, column=2, padx=(0, 15), pady=10)

button_quit = Button(window, text="Quit", image=img_start,
                     width=50, height=40, command=quit)
button_quit.config(relief="raised")
button_quit.configure(background="gray")
button_quit.grid(row=2, column=2, padx=(0, 15), pady=10)

text = StringVar()


display = Text(window, width=50, height=10)
display.config(relief="sunken")
display.configure(background="lightgray")
display.grid(row=6, column=4, pady=(0, 0))

scrollbar = Scrollbar(window, command=display.yview)
scrollbar.grid(row=6, column=3, sticky="nsew")

""" with StringIO as output:
    print("Hello world", file=output)
    text.set(output.getvalue())
 """


window.mainloop()
