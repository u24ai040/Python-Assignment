number=int(input("Enter the Number:"))
i=0
sum=0
while number > 9:  # Continue until it's a single digit
     sum_digits = 0
     while number > 0:
        sum_digits += number % 10
        number //= 10
     number = sum_digits
print("Digital Root : ",number)