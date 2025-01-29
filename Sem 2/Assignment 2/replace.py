def replace(string,old,new):

    result=''
    i=0
    old_length=len(old)

    while(i<len(string)):
           if string[i:i+old_length] == old:
            result += new  
            i += old_length  
           else:
            result += string[i] 
            i += 1 
    return result
        
string=input("Enter the String :")
old=input("Enter string you want to replace :")
new=input("Enter string by which you want to replace :")

result=replace(string,old,new)

if result==string:
   print("Given old string is not found or do not enter same  as old ")
   print(result)
else:
   print(result)

