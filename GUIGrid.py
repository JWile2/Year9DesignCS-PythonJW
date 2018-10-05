#tkinter is a tool box that holds code that you can use
import tkinter as tk 

# root is a variable that holds the information
#about the main window, That is the window with the
#close, min, max buttons in the top left
root = tk.Tk()#tk.Tk() go in the tk tool box and use the function Tk()

ent = tk.Entry(root)
ent.grid(row = 0, column = 0)

btn = tk.Button(root, text = "Press Me")
btn.grid(row = 0, column = 1)

label = tk.Label(root, text = "...")
label.grid(row = 1, column = 0, columnspan = 2)

# sets up your program in an infinit loop waiting
#for the user to do something. This is an EVENT
#DRIVE PROGRAM. This means a function is called when we "do something"
root.mainloop()