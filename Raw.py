# Calculations


def Total_Marks():

    Total = Subject_1 + Subject_2 + Subject_3
    return Total


def Average():

    Avg = Total_Marks() / 3
    return Avg


def Grade(mark):

    if mark >= 75 and mark <= 100:
        grade = "A"

    elif mark >= 65 and mark < 75:
        grade = "B"

    elif mark >= 50 and mark < 65:
        grade = "C"

    elif mark >= 0 and mark < 50:
        grade = "F"

    else:
        grade = "Invalid Marks !!!"

    return grade


def Result():

    if Average() >= 50:
        result = "Pass"
    else:
        result = "Fail"

    return result


# Statements


print("--Welcome To Student Result Calculator--")
print("----------------------------------------")

# Inputs

Student_Name = input("Enter Your Name : ")
Subject_1 = float(input("Enter Your Subject 1 Marks : "))
Subject_2 = float(input("Enter Your Subject 2 Marks : "))
Subject_3 = float(input("Enter Your Subject 3 Marks : "))

print("------------------------------------")

print(f"Hello {Student_Name},")
print("This is Your Result Summary")
print("------------------------------------")

print(f"Total\t= {Total_Marks()}")
print(f"Average\t= {Average()}")
print(
    f"Grade\t= Subject 1 - {Grade(Subject_1)}, Subject 2 - {Grade(Subject_2)}, Subject 3 - {Grade(Subject_3)}"
)
print(f"Result\t= {Result()}")
print("------------------------------------")
print("Thank You")
