def Is_Fibbo(n):
    if n == 0 or n == 1:
        return True
    
    a, b = 0, 1
    while b < n:
        a, b = b, a + b 
        if b == n:
            return True
    return False

T = int(input("Enter the Number of Test Case Data: "))
results = []

for _ in range(T):
    n = int(input("Enter the number: "))
    results.append("IsFibbo" if Is_Fibbo(n) else "IsNotFibbo")


for i in results:
    print(i)
