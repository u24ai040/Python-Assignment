number=int(input("Enter the number : "))
reverse=0
while (int(number)) >0:
    (reminder)=int(number)%10
    reverse=(reminder) + reverse*10
    number/=10
print("Reverse of the given number = ",reverse)