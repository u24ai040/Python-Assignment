list_Number=[]
for i in range(0,50):
            list_Number.append(i)

list_Square=[]
for i in range(0,51):
        list_Square.append(i*i)

list_Alphabets=[]

for i in range(1,27):
    
    for j in range (1,i+1):
        str=chr(96+i) * j

    list_Alphabets.append(str)
    

print(list_Number)
print(list_Square)    
print(list_Alphabets)
    
        