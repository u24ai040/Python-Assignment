#QUESTION 5

import numpy as np

arr=[]
n=int(input("Enter the number of words: "))
for i in range(n):
    word=input("Enter the word: ")
    arr.append(word)

arr = np.array(arr)


for word in arr:
    centered = word.center(15, '_')
    left_justified = word.ljust(15, '_')
    right_justified = word.rjust(15, '_')

    
    print(f"Original    : {word}")
    print(f"Centered    : {centered}")
    print(f"Left Justified : {left_justified}")
    print(f"Right Justified: {right_justified}")
    print("-" * 40)#
