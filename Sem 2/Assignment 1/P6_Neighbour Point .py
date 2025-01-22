#Function to find distance between  two points
def distance_between_points(x1,y1,z1,x2,y2,z2):
    return ((x2-x1)*(x2-x1)+ (y2-y1)*(y2-y1) + (z2-z1)*(z2-z1))

points = list(range(10))
for i in range(10):
    print("Enter Coordinates for point ",i+1)
    x = int(input("Enter x coordinate: "))
    y = int(input("Enter y coordinate: "))
    z = int(input("Enter z coordinate: "))
    points[i] = (x,y,z)

Nearest_Neighbour_point=[]

for i in range(0,10):
    min_distance=float('inf')
    Current_Point=points[i]
    nearest_point=None
    for j in range(0,10):
        Other_Point=points[j]
        if i==j :
            continue
        else :
            Currrent_Distance=distance_between_points(Current_Point[0],Current_Point[1],Current_Point[2],Other_Point[0],Other_Point[1],Other_Point[2])
            if Currrent_Distance<min_distance:
                min_distance=Currrent_Distance
                nearest_point=Other_Point
    Nearest_Neighbour_point.append((Current_Point,nearest_point))#Storing Point and it's nearest point in form of tupple in list

print("Output:\n")
print("Point         Nearest point")
for ((Current_Point,nearest_point)) in Nearest_Neighbour_point:
    print((Current_Point,nearest_point))
