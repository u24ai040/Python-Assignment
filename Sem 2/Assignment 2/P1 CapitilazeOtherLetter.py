word=input("Enter the word :")
result=''#string to store a output
for i in range(0,len(word)):
    if i%2!=0:
        result+=word[i].upper()#if index is odd then letter should be capitilize
    else:
        result+=word[i].lower()

print(result)