#counting minimum number of swaps to sort a list
swapCounter =0
n =int ( input("Enter the size of list:"))
original_list = []
for i in range(n):
    original_list.append((int(input("Enter the number: ")),i))

print ("List of Hight: " ,list)
sorted_list = sorted(original_list)#Sorting the list and storing the element in list and its index

print("Sorted list : " ,sorted_list)

i =0
while i <n:
    if(original_list[i][1] == sorted_list[i][1]):
        i+=1
    else:
        temp=0
        temp=original_list[i]
        original_list[i]=original_list[sorted_list[i][1]]
        original_list[sorted_list[i][1]]=temp
        swapCounter+=1
        i+=1

print("Minimum Number of Swaps : ",swapCounter)