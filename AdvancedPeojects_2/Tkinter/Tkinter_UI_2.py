from tkinter import *

root = Tk()

Button1 = Button(None, text="Click Me!", fg="Blue")
Button1.pack()
Button2 = Button(None, text="Click Me!", fg="Blue")
Button2.pack(fill=X)
Button3 = Button(None, text="Click Me!", fg="Blue")
Button3.pack()
Button4 = Button(None, text="Click Me!", fg="Red")
Button4.pack(fill=Y)
root.mainloop()
