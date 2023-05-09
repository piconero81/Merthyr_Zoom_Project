from tkinter import *
from tkinter import ttk
#Create an instance of Tkinter frame
root = Tk()
#Set the geometry of Tkinter frame
root.geometry("700x270+600+500")
w = 900 # width for the Tk root
h = 650 # height for the Tk root


def Close():
    root.destroy()

Label(root, text=" Please do not use Mouse and Keyboard while Zoom is Loading....", font=('Helvetica 14 bold')).pack(pady=20)
#Create a button in the main Window to open the popup
ttk.Button(root, text= "Close", command= Close).pack()
root.mainloop()