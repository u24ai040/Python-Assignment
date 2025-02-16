L=int(input("Enter L:"))
R=int(input("Enter R:"))
Max=0
min=0
for i in range(L,R+1):
    for j in range(i,R+1):
        
        Max=i^j
        xor=max(Max,min)
        min=xor

print(xor)
