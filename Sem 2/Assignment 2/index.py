def index(string,substring):
    sub_length=len(substring)
    i=0
    while(i<len(string)):
        if string[i:i+sub_length]==substring:
            flag= i
            break
        else :
            flag=0
        i+=1
    return flag

string=str(input("Enter the String :"))
substring=str(input("Enter the substring you want to search :"))
count=index(string,substring)
if count!=0:
    print(count)
else:
    print("Substring is not present in string.")
