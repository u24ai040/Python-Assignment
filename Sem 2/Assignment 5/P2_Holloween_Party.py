def maximum_pieces(k):
    if k%2:
        i=(k-1)/2
        j=i+1
        return i*j
    else:
        return k*k/4

T=int(input("Enter the number of test cases:"))
Maximum=[]
for i in range(T):
    k=int(input("Enter the value of K:"))
    Max=maximum_pieces(k)
    Maximum.append(Max)
for i in Maximum:
    print(i)