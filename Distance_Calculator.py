import math
print("This program is to calculate the distance between two given points (x1, y1) and (x2, y2) on a 2D plane")
print(' ')
print("Please enter your chosen numbers for each point:")
x1 = int(input("Point x1: "))
y1 = int(input("Point y1: "))
x2 = int(input("Point x2: "))
y2 = int(input("Point y2: "))
Pow = math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2)
Distance = math.sqrt(Pow)
print(f"The distance between {x1}, {y1}, {x2} and {y2} is: {Distance: .2f}")

