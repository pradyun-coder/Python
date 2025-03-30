from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

window = Tk()
window.title("RPS Game")
window.geometry("550x450")
size = (150, 250)

def ROCK():
    choices = ["Rock", "Paper", "Scissor"]
    chosen = random.choice(choices)
    if chosen == "Rock":
        messagebox.showinfo("Result!", "It's a tie! I chose Rock too")
    if chosen == "Paper":
        messagebox.showinfo("Result!", "You lost! I chose Paper")
    if chosen == "Scissor":
        messagebox.showinfo("Result!", "You won! I chose Scissor")

def PAPER():
    choices = ["Rock", "Paper", "Scissor"]
    chosen = random.choice(choices)
    if chosen == "Rock":
        messagebox.showinfo("Result!", "You won! I chose Rock")
    if chosen == "Paper":
        messagebox.showinfo("Result!", "It's a tie! I chose Paper too")
    if chosen == "Scissor":
        messagebox.showinfo("Result!", "You lost! I chose Scissor")

def SCISSOR():
    choices = ["Rock", "Paper", "Scissor"]
    chosen = random.choice(choices)
    if chosen == "Rock":
        messagebox.showinfo("Result!", "You lost! I chose Rock")
    if chosen == "Paper":
        messagebox.showinfo("Result!", "You won! I chose Paper")
    if chosen == "Scissor":
        messagebox.showinfo("Result!", "It's a tie! I chose Scissor too")

scissor = Image.open("SCISSOR.png")
scissor = scissor.resize(size)
SCISSORimage = ImageTk.PhotoImage(scissor)

rock = Image.open("ROCK.png")
rock = rock.resize(size)
ROCKimage = ImageTk.PhotoImage(rock)

paper = Image.open("PAPER.png")
paper = paper.resize(size)
PAPERimage = ImageTk.PhotoImage(paper)

SCISSORbutton = Button(window, image=SCISSORimage, command = SCISSOR)
SCISSORbutton.place(x = 25, y = 150)

ROCKbutton = Button(window, image=ROCKimage, command = ROCK)
ROCKbutton.place(x = 200, y = 150)

PAPERbutton = Button(window, image=PAPERimage, command = PAPER)
PAPERbutton.place(x = 375, y = 150)

window.mainloop()