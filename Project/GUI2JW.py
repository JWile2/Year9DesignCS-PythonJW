

import tkinter as tk 


root = tk.Tk()
########   Quiz Code
titlelabel = tk.Label(root, text = "MATH QUIZ", font=("Helvetica",16), background = "blue", foreground = "white")
titlelabel.grid(row = 0, column = 0, columnspan = 2)


output = tk.Text(root, height = 10, width = 50)
output.config(state = "disable")
output.grid(row = 1, column = 0, columnspan = 2)

word1Label = tk.Label(root, text = "7 x 7", foreground = "blue")
word1Label.grid(row = 2, column = 0, sticky = "NESW")

word2Label = tk.Label(root, text = "8 x 8 x 2", foreground = "blue")
word2Label.grid(row = 3, column = 0)

word3Label = tk.Label(root, text = "63 x 2", foreground = "blue")
word3Label.grid(row = 4, column = 0)


ent1 = tk.Entry(root)
ent1.grid(row = 2, column = 1)

ent2 = tk.Entry(root)
ent2.grid(row = 3, column = 1)

ent3 = tk.Entry(root)
ent3.grid(row = 4, column = 1)

btnGo = tk.Button(root, text = "CHECK ANSWERS")
btnGo.grid(row = 5, column = 1,)


questionFrame = tk.LabelFrame(root,text = "Question")
questionFrame.grid(row = 0, column = 0)

calcFrame = tk.LabelFrame(root,text = "Calculator")
calcFrame.grid(row = 0, column = 2)

#****************Question Frame


def bttnClicked():
	num1 = input("Enter a number:")
	num2 = input("Enter a number:")

	result = int(num1) * int(num2)
	print (result)

#****************Calc Frame
cfBtn1 = tk.Button(calcFrame,text = "Button", command = bttnClicked)
cfBtn1.pack()

root.mainloop()

