
Test_case=int(input("Enter the number of test cases :"))
#N is No of boxes,initially Coin was in Xth Box,S is the no of swaps
for i in range(Test_case):

    N,X,S=map(int,input().split())
    
    Coin_Position=X

for i in range(S):
    A,B=map(int,input().split())
    if  Coin_Position==A:
         Coin_Position=B
         print("After Swaping coin will be in : ",B)

    elif  Coin_Position==B:
         Coin_Position=A
         print("After Swaping coin will be in : ",A)
         
    else:
        print("Invalid Input")

