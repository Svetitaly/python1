# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Benvenuti al corso python")
# Set geometry (widthxheight)
root.geometry('500x500')
# adding a label to the root window
lbl = Label(root, text="Sei tu un developer?")
lbl.grid()

# Execute Tkinter
root.mainloop()
# all widgets will be here