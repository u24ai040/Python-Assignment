def SherlockSquares(A,B):
    a=int(A**0.5)
    b=int(B**0.5)

    if a*a<A:
        a+=1
    count=0
    num=a
    while(num <=b):
        count+=1
        num+=1

    return count


T=int(input("Enter the Number of Testcases :"))
result=[]
for i in range(T):
    A=int(input("Enter the A:"))
    B=int(input("Enter the B:"))
    if A<=0 or B<=0:
        print("Enter non zero Positive Integer:")
        break
    else:
        flag=SherlockSquares(A,B)
        result.append(flag)

for i in result:
    print(i)