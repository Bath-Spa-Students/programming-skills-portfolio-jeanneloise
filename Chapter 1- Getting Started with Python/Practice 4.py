
import math 
def triangle_area_heron(a, b, c):
    s= (a+b+c)/2
    area= math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area
a=float(input("Enter the first side if lenght of the triangle:"))
b=float(input("Enter the second side lenght of the triangle:"))
c=float(input("Enter the third side lenght of the triangle:"))
print("The area of the triangle is", triangle_area_heron(a, b, c))

