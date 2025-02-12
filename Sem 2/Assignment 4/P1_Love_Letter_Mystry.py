def palindrom(str):
    i=1
    j=len(str)
    count=0
    while i<=j:
        count+=abs(ord(str[i-1])-ord(str[j-1]))
        i+=1
        j-=1
    return count


T=int(input("Enter the number of test cases :"))
result=[]
for i in range(T):
    string=input("Enter the string :")
    flag=palindrom(string)
    result.append(flag)

for i in result:
    print(i)