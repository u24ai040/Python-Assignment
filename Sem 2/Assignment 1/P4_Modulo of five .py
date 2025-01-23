# Initialize sets for the equivalence classes
class_0 = set()
class_1 = set()
class_2 = set()
class_3 = set()
class_4 = set()
Universal=set()

for num in range(1, 10001):
    Universal.add(num)
    remainder = num % 5
    if remainder == 0:
        class_0.add(num)
    elif remainder == 1:
        class_1.add(num)
    elif remainder == 2:
        class_2.add(num)
    elif remainder == 3:
        class_3.add(num)
    elif remainder == 4:
        class_4.add(num)

# Output the equivalence classes
print("when reminder is 0 Equivalence class [0] :")
print(sorted(list(class_0))[:15])  #To print First 15 elements
print("...")
 
print("")

print(" when reminder is 1 Equivalence class [1] :")
print(sorted(list(class_1))[:15]) #To print First 15 elements
print("...")
print("")

print("when reminder is 2 Equivalence class [2] :")
print(sorted(list(class_2))[:15])   #To print First 15 elements
print("...")
print("")

print("when reminder is 3 Equivalence class [3] :")
print(sorted(list(class_3))[:15])   #To print First 15 elements
print("...")
print("")

print("when reminder is 4 Equivalence class [4] :")
print(sorted(list(class_4))[:15])  #To print First 15 elements 
print("...")

class_0.update(class_1)
class_0.update(class_2)
class_0.update(class_3)
class_0.update(class_4)

if Universal==class_0:
    print("All classes are valid")
    print("Unioun of all classes is Universal or Original")
else:
    print("Classes are not valid")
