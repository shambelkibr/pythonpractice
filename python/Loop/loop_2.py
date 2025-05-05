count_even=0
sum=0
i=1
for i in range(11):
    if i % 2==0:
        count_even=count_even+1
        sum+=i
print(f"the frist {count_even} number between 1 and 10 sum  is {sum}")        