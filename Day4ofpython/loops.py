#sometime we wants to repeat statement in our program 
#loops make it easy  for programmer what to repeate and how
#there are two types of loops in python
#1 while loops
#2 for loops
'''
WHILE LOOP 
Syntax: 
while (condition): # The block keeps executing until the condition is true 
#Body of the loop 
In while loops, the condition is checked first. If it evaluates to true, the body of the loop 
is executed otherwise not! 
If the loop is entered, the process of [condition check & execution] is continued until 
the condition becomes False.
'''
i = 0
while i < 5:
    print("harry")
    i =i + 1
print(i)

list = []
while len(list)<5:
    print("parvez")
    list.append(1)
print(list)

#for loop
l =["parvez",50,"santanu",78]
for item in l:
    print(item)

#range() function in python
#range() in python is used to generate a sequence of number
#we can also specifie the start, stop, and step_size as follow
#range(start, stop, step_size)
a =0
for a in range(0, 7):
    print(a)
for a in range(0, 20, 5):
    print(a)
else:
    print("done")#we can also use else with for loop

