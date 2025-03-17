from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('Displaying images')
root.geometry('400x400')

upload = Image.open("aircraft.png")
image = ImageTk.PhotoImage(upload)

label = Label(root, image = image, height = 350, width = 300)
label.place(x = 50, y = 50)
label2 = Label(root, text = "This is a demonstration regarding inculcation of images")
label2.place(x = 50, y = 50)
def msg():
    messagebox.showwarning("Alert! Viruses have been detected")
button = Button(root, text = "Scan for Viruses", command = msg)
button.place(x = 150, y = 0)

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("New Window")
    label3 = Label(top, text = "This is the new window")
    label3.pack()
label4 = Label(root, text = "Below is the button to open a new window")
btn = Button(root, text = "Click here", command = topwin)
label4.pack()
btn.pack()
root.mainloop()