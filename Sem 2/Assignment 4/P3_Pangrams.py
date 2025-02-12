def pangrams(str):
    str=str.lower()
    alphabets=set("abcdefghijklmnopqrstuvwxyz")
    flag=alphabets.issubset(set(str))
    return flag


T=int(input("Enter the number of test cases :"))
result=[]
for i in range(T):
    string=input("Enter the string :")
    flag=pangrams(string)
    result.append(flag)

for i in result:
    if i==True:
        print("String is pangram")
    else:
        print("String is not pangram")


