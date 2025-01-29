number=int(input("Enter the number of products :"))

dict={}
for i in range(0,number):
    Product_Name=str(input("Enter Product Name :"))
    Product_Price=str(input("Enter Product Price :"))
    dict[Product_Name]=Product_Price

name=str(input("Enter Product name to check:"))

if name in dict:
    print(dict.get(name))
else:
    print("Product is not in dictionary")