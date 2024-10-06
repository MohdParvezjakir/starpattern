# write a program to find whether a given number is a prime number or not 
number=int(input("Enter your number:"))
for i in range(2, number):
    if(number%i) ==0:
        print("number is not prime")
        break
else:
        print("number is prime")

#write a program to find the sum of first n natural numbers using while loop 

n = int(input("Enter the number: "))
i = 1
sum = 0
while(i<=n):
    sum += i
    i+=1

print(sum)


