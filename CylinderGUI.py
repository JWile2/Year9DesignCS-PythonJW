import tkinter as tk
import math

def submit():
	print("Submit pressed")
	r = float(entr.get())
	h = float(enth.get())

	v = math.pi*r*r*h
	v = round(v,3)
	output.config(state="normal")
	
	outputValue = "Given\nradius:"+str(r)+" units\nheight"+str(h)+" units\nThe volume is"+str(v)+" units cubed\n\n"


	out.elete(1.0,tk.END)
	output.insert(tk.INSERT,outputVolume)
	output.config(state="disabled")



#Input
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

btn = tk.Button(root, text="Submit", command=submit)
btn.pack()

#width = 50, height = 10 are called named parameters. 
output = tk.Text(root, height =10, width = 50, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()







root.mainloop()