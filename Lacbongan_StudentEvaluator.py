#Global Variables

header1 = ("STUDENT PERFORMANCE EVALUATOR")
header2 = ("STUDENT PERFORMANCE REPORT")

#Getting information
print(header1)
Name = input("Enter your name: ")
A1 = int(input("Enter Assessment 1: "))
A2 = int(input("Enter Assessment 2: "))
A3 = int(input("Enter Assessment 3: "))
Sum = A1 + A2 + A3
Average = Sum / 3

def get_student_info():
    print(Name)
    print(A1)
    print(A2)
    print(A3)
    print(Sum)
    print(Average)

#Calculation stage
def evaluate_performance():
    if 90 <= Average <= 100:
         print("Performance Level: Outstanding!")
    elif 85 <= Average <= 90:
         print("Performance Level: Very Satisfactory!")
    elif 80 <= Average <= 85:
         print("Performance Level: Satisfactory!")
    elif 75 <= Average <= 80:
         print("Performance Level: Fairly Satisfactory")
    else:
         print("Performance Level: Needs Improvement.")

def display_report():
    print("Student Name: ", Name)
    print("Assessment Scores: ", A1, A2, A3)
    print(f"Average Score: {Average:.2f}")

#Display outputs
print(header2)

get_student_info()
evaluate_performance()
display_report()