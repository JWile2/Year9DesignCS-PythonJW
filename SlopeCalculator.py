import os
print("Slope Calculator:")
os.system("say hello welcome to my slope calculator")
#Input
x1 = input("Input x1: ")
x1 = int(x1)

y1 = input("Input y1: ")
y1 = int(y1)

x2 = input ("Input x2: ")
x2 = int(x2)

y2 = input ("Input y2: ")
y2 = int(y2)


#Process
rise = x2 - x1
run = y2 - y1
fslope = rise/run
#Output
print("Your slopeis m = "+str(rise)+"/"+str(run))
print ("Your slope as a decimal is ",fslope)
print(rise)
print(run)
os.system("say Your slope is m = "+str(rise)+"/"+str(run))
os.system("say Your slope as a decimal is ",fslope)