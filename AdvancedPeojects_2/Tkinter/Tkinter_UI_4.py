from tkinter import *

root = Tk()

def printName(event):
    print("Hello Matarata")

button = Button(root, text="Click me")
button.bind("<Button-1>", printName)
button.pack()

root.mainloop()