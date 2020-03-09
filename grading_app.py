

def grade(num):
    class_average = num
    if class_average >= 90:
        return "Your grade is an A"
    elif class_average >= 80:
        return "Your Grade is a B"
    elif class_average >= 70:
        return "Your Grade is a C"
    elif class_average >= 60:
        return "Your Grade is a D"
    else:
        return "You did not pass this class"

try:
    num = float(input("Enter your Grade: "))
    print(grade(num))
except ValueError:
    print("Please enter an appropriate character")