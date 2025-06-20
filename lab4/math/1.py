#1 task 
import math

degree = float(input("Input degree: "))

radian = math.radians(degree)

print("Output radian:", round(radian, 6))

#2 task
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = ((base1 + base2) * height) / 2

print("Expected Output:", area)

#3 task
num_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

area = (num_sides * (side_length ** 2)) / (4 * math.tan(math.pi / num_sides))

print("The area of the polygon is:", round(area, 2))

#4 task
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height

print("Expected Output:", area)