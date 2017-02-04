from tkinter import *

root = Tk()

label1 = Label(root, text = "Name: ")
label2 = Label(root, text = "Password: ")
label1.grid(row = 0, column = 0, sticky="E")
label2.grid(row = 1, column = 0,sticky="E")
entry = Entry(root,)
entry.grid(row = 0, column = 1)
entry2 = Entry(root,)
entry2.grid(row = 1, column = 1)
checkButton = Checkbutton(root, text="Remember me!")
checkButton.grid(columnspan = 2)

root.mainloop()