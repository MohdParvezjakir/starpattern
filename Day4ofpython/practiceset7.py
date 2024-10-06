# Write a program to print multiplication table of a given number using for loop.
number=int(input("Enter your number:"))
l=[]
l.append(number)
for item in l:
    print(item,(item * 2),(item *3),(item *4),(item *59),(item *6),(item *7),(item *8),(item *9),(item *10))
else:
    print("done")
#or
n=int(input("enter your number:"))
for i in range(0,11):
    print(f"{n} x {i} = {n*i}")
else:
    print("done")


# Write a program to greet all the person names stored in a list ‘l’ and which starts 
# with S. 
name1=input("Enter your name:")
list=[]
list.append(name1)
for item in list:
    if item.startswith("s")==True:
        print(f"hello,{name1}")
    else:
        print("your name is not start with s")
    print(list)


#or
list2=["harry","parvez","paneer","pratham"]
for name in list2:
    if name.startswith("p"):
        print(f"hello,{name}")

#attemp problem1 using while loop
n2=int(input("Enter your number:"))
i=0
while i<11:
    print(f"{n2} x {i} = {n2*i}")
    i=1 + i





