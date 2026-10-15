#Num1 and Num2 are both global variables
Num1 = float(input("Enter a number: "))
Num2 = float(input("Enter another number: "))

def calculate_sum(num1, num2):
    #Sum is our first local variable
    sum = num1 + num2
    print("Sum: ", sum)

def calculate_difference(num1, num2):
    #Difference is the second local variable
    difference = num1 - num2
    print("Difference: ", difference)

calculate_sum(Num1, Num2)
calculate_difference(Num1, Num2)