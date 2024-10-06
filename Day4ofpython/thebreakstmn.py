#break in used to comeout to the loop when encountered! it instructs to program  exit from the loop now
a=0
for a in range(0, 80):
    print(a)
    if (a==9):
        break
#the continue is used to skip current iteration of loop
b=0
for b in range(0, 56):
    if (b==5):
        continue
    print(b)
#pass is null statement in python
# it instructs "do nothing" to program
l=0
for l in range(5):
    pass #without pass it throw a error
    
    

    
        
