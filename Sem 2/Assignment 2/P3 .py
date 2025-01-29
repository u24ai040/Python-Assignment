number=int(input("Enter the number : "))
i=0
count=0
original=number

while number!=0:
    m=number%10
    number//=10
    if m!=0:
        if original%m==0:
            count+=1
    else:
        continue
    
    
print(count)
