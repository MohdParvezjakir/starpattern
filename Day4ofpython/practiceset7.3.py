#write a program to calculate factorial of a given number using for loop
n=int(input("Enter your number:"))
product=1
for i in range(1,(n +1)):
    product=product *i

print(f"the fectorial of{n} is {product}")
