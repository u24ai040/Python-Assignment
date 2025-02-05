def Utopian_Tree_Height(N):
    height = 1  
    for cycle in range(1, N + 1):
        if cycle % 2 == 1: 
            height *= 2
        else:            
            height += 1
    return height


T = int(input("Enter the number of test cases: "))
results=[]
for _ in range(T):
    N = int(input("Enter the number of cycles: "))
    h=Utopian_Tree_Height(N)
    results.append(h)
for i in results:
    print(i)
