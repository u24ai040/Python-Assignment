def count(string,substring):

    sub_length=len(substring)
    i=0
    counts=0
    while(i<len(string)):
        if string[i:i+sub_length]==substring:
            counts+=1
        i+=1
    return counts

string=str(input("Enter the String :"))
substring=str(input("Enter the substring you want to search :"))
counts1=count(string,substring)
if counts1>0:
    print(counts1)
else:
    print("Substring is not present in string.")



