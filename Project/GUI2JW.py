
import tkinter as tk 
import random
def checkanswerfnc(*args):
	print ("CheckAnswer")
root = tk.Tk()
########   Quiz Code

#****************Question Frame
#We need to store the actual questions
#We can randomzie the questions by doing the following
operators = ["+","-","*","/"]
q1 = []
q1.append(random.randint(1,12))
opt = operators[random.randint(0,3)]
q1.append(opt)
q1.append(random.randint(1,12))
print(q1)

question1 = ""

q2 = []
q2.append(random.randint(1,12))
opt = operators[random.randint(0,3)]
q2.append(opt)
q2.append(random.randint(1,12))
print(q2)

question2 = ""

q3 = []
n = random.randint(1,12)
x = random.randint(1, 5)
q3.append(n*x)
opt = operators[3]
q3.append(opt)
q3.append(n)
print(q3)

question3 = ""


def bttnClicked(*args):

	print("bttnClicked")

	'''num1 = input("Enter a number:")
	num2 = input("Enter a number:")

	result = int(num1) * int(num2)
	print (result)'''
#ansR = int(0)

def checkAnswerfnc(*args):
	print(q1)
	print(q2)
	print(q3)


	#Check Question 1
	if(q1[1] == "*" and q1[0] * q1[2] == int(ent1.get())) or (q1[1] == "-" and q1[0] - q1[2] == int(ent1.get())) or (q1[1] == "+" and q1[0] + q1[2] == int(ent1.get())) or (q1[1] == "/" and q1[0] / q1[2] == int(ent1.get())): 
		print("Question 1 Correct")
		#ansR = ansR +1
	if(q2[1] == "*" and q2[0] * q2[2] == int(ent2.get())) or (q2[1] == "-" and q2[0] - q2[2] == int(ent2.get())) or (q2[1] == "+" and q2[0] + q2[2] == int(ent2.get())) or (q2[1] == "/" and q2[0] / q2[2] == int(ent2.get())): 
		print("Question 2 Correct")
		#ansR = ansR +1

	if(q3[1] == "*" and q3[0] * q3[2] == int(ent3.get())) or (q3[1] == "-" and q3[0] - q3[2] == int(ent3.get())) or (q3[1] == "+" and q3[0] + q3[2] == int(ent3.get())) or (q3[1] == "/" and q3[0] / q3[2] == int(ent3.get())): 
		print("Question 3 Correct")
		#ansR = ansR +1






titlelabel = tk.Label(root, text = "MATH QUIZ", font=("Helvetica",16), background = "blue", foreground = "white")
titlelabel.grid(row = 0, column = 0, columnspan = 2)


output = tk.Text(root, height = 10, width = 50)
output.config(state = "disable")
output.grid(row = 1, column = 0, columnspan = 2)
question = ""
for i in range(0, len(q1),1):
	question = question + str(q1[i])
for i in range(0, len(q2), 1):
	question2 = question2 + str(q2[i])
for i in range(0, len(q3),1):
	question3 = question3 + str(q3 [i])

word1Label = tk.Label(root, text = question, foreground = "blue")
word1Label.grid(row = 2, column = 0, sticky = "NESW")

word2Label = tk.Label(root, text = question2 ,foreground = "blue")
word2Label.grid(row = 3, column = 0)

word3Label = tk.Label(root, text = question3 , foreground = "blue")
word3Label.grid(row = 4, column = 0)


ent1 = tk.Entry(root)
ent1.grid(row = 2, column = 1)

ent2 = tk.Entry(root)
ent2.grid(row = 3, column = 1)

ent3 = tk.Entry(root)
ent3.grid(row = 4, column = 1)

btnGo = tk.Button(root, text = "CHECK ANSWERS", command = checkAnswerfnc)
btnGo.grid(row = 5, column = 1,)


questionFrame = tk.LabelFrame(root,text = "Question")
questionFrame.grid(row = 0, column = 0)



logo = tk.PhotoImage(file = "Math2.png")
logoImage = tk.Label(image = logo)
logoImage.config(background = "white")
logoImage.grid(row = 0, column = 1, columnspan = 1)


root.mainloop()
