list=[]

for i in (0,3):
    name=str(input("Enter name :"))
    if len(name)>15:
        name =name[0:16]#Slicing to 
    name = name[::-1]#Reverse the name
    list.append(name)
    
    
    print(list)

