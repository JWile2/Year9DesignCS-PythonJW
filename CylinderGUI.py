import tkinter as tk

root = tk.Tk()
root.title("Volume of a Cylinder")

labr = tk.Label(root, text="radius")
labr.pack()

entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root, text="height")
labh.pack()

enth = tk.Entry(root)
enth.pack()

btn = tk.Button(root, text="Submit")
btn.pack()

#width = 50, height = 10 are called named parameters. 
output = tk.Text(root, height =10, width = 50, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()

root.mainloop()