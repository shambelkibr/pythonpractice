n=int(input("enter your check number"))
counts=0
for i in range(1,n):
   if n%i==0:
       counts=counts+1
       print(i)
if counts>2:
    print(f"the number is prime {n} is multiples {counts}")
else:
    print("not prime ")
    
    
fact=1
n=int(input("enter the number:= "))
for i in range(n):
    if i==0:
      fact=1
    else:
     fact=fact*i
    
print(fact)