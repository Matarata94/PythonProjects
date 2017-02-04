from tkinter import *

root = Tk()
topFrame = Frame(root)
topFrame.pack()
botFrame = Frame(root)
botFrame.pack(side=BOTTOM)

Label1 = Label(root, text="This is our first label")
Label1.pack()
Button1 = Button(topFrame, text="Click Me!", fg="Blue")
Button1.pack(side=LEFT)
Button2 = Button(topFrame, text="Click Me!", fg="Blue")
Button2.pack(side=RIGHT)
Button3 = Button(botFrame, text="Click Me!", fg="Blue")
Button3.pack(side=LEFT)
Button4 = Button(botFrame, text="Click Me!", fg="Red")
Button4.pack(side=RIGHT)
root.mainloop()
