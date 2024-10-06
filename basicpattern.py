#the pattern mainly have two things space and character which programmer used to pattern like *, #, $ etc.
#example
# _______*
# ______***
# _____*****
#this program is fo4r a simple squre pattern
n=int(input("Enter rows number"))#for size of pattern
for i in range(n): #rows number
    for j in range(n): #collon number
        print("*",end=" ") #print the character
        
    print()
#write a program for increasing triangle
for i in range(n):
    for j in range(i+1):
        print("*",end='_')
    print()
#program for decreasing triangle
for i in range(n):
    for j in range(i, n):
        print("*",end=" ")
    print()
#program for a increasing  right side triangle
for i in range(n):
    for j in range(i, n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
#program for decresing right side triangle
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
#write a program for a hill pattern 
for i in range(n):
    for j in range(i, n):
        print(" ",end=" ")
   # for j in range(i+1): here we will use only i rather than i+1 otherwise hill will be topless
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
# program for a reverse hill 
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i, n-1):
        print("*",end=" ")
    for j in range(i, n):
        print("*",end=" ")
    print()
# program adiamond shape pattern
for i in range(n-1):
    for j in range(i, n):
        print(" ",end=" ")
    for j in range(i):
        print("$",end=" ")
    for j in range(i+1):
        print("$",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i, n-1):
        print("*",end=" ")
    for j in range(i, n):
        print("*",end=" ")
    print()

#write a program for a empty box 
for i in range(n):
    if (i==1 or i==n):
        for j in range(i+1):
            print("*", end=" ")
    else:
        for j in range(i+1):
            print(" "* (n-2),end=" ")
    print()

