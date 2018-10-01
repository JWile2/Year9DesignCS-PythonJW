#A loop structure is a structure that allows us to run 
#a section of code a number of times.
#It is great for when we need to repeat a process. It is also great
#when we need to run a pattern. 

#There are two broad categories of loops
# Conditional loop: this loops as long as something is true
#Counted loop: This loops a set of numbers 0 times

print("0")
print("1")
print("2")
print("3")
print("4")
print("5")

print("********************")
#The general structure of a counted loop is
#Count: This is a variable we use to track the number of
# 	times a loop runs
#Check: this is the boolean (true or false) statement we evaluate
#	to decide if we keep going
#Change: This is the change in the count that happens after each
#	loop.each

#We use a for i in range loop
for i in range(0,6,1):
	print(i)

#How would the above loop run
#We would reach line 27

# i = 0,0 < 6, True RUN LOOP
# i = 1,1 < 6, True RUN LOOP
# i = 2,2 < 6, True RUN loop

print("**************")
print("write a loop that will print out 7 to 104 inclusive")
for i in range(7,105,1):
	print(i)

print("write a loop that will print out even numbers from -22 to 134 inclusive")
for i in range(-22, 135, 2):
	print(i)

print("************")
print("We can count backwards as well. Python3 will asume the check based on")
print("relative value of the count and the check")

for i in range(3,0,-1):
	print(i)

print("*************")
print("Print out all numbers from 101 to 0 inclusive")
for i in range(101,-1,-1):
	print(i)
print("*******")
print("print out all numbers from 1 to 8 inclusive")

s = "Fish food"
#Best YOU MUST DO THIS: NEVER NEVER NEVER TYPE IN LENGTH OF STRING AS
#A NUMBER. ALWAYS HAVE THE COUMPUTER FIND IT
for i in range(0,len(s),1):
	print(s[i])
print("***************")
#Can you print out s in reverse
for i in range(8,-1,-1):
	print(s[i])

print("********************")
#Can you print every second letter starting at index 0
for i in range(0,len(s),2):
	print(s[i])