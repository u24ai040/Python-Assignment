#QUESTION 2

import pandas as pd
s=pd.Series()
n=int(input(("Enter number of strings: ")))
for i in range(n):
    print("Enter string ", i+1, ":")
    string=input()
    s[i]=string
    

s = s.str.upper()
print(s)

s = s.str.lower()
print(s)

s=s.str.len()
print("Length of each string in the series:")
print(s)