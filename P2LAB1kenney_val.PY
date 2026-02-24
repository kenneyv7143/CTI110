# Valerie L.Kenney  
# Date2/24/2026
# P2LAB1
# Computing diameter,circumference,area of a  circle
#import the math library for the constant pi
import math
# get radius from user
print()
radius = float(input("What is the radius of the circle? "))
print()
#calculate diameter
diameter= 2 * radius
# calculate the circumference
circumference = 2 * radius * math.pi 
# calculate the area
area =  math.pi * radius**2
print (f"The diameter of the circle is {diameter:.1f}\n")
print (f"The area of the circle is {radius * 2:.1f}\n")
print (f"The circumference of the circle is {radius:.1f}\n")
