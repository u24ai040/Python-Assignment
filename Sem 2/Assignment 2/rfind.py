def rfind(string,substring,start,end):
    m=0
    i=end-1
    sublength=len(substring)
    st=start
    while i>=st and i<end:
         start=i-sublength+1
         if string[start:i+1]==substring:
            flag= i
            break
         else:
            flag=-1
         i-=1
    return flag
    

string=str(input("Enter the String:"))
substring=str(input("Enter Substring:"))
start=int(input("Enter the starting index :"))
end=int(input("Enter the end :"))
count=int(rfind(string,substring,start,end))
if (count+1 )!=0:
    print(count)
else:
    print("Substring is not present in string.")
