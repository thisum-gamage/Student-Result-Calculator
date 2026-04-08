# Functions


def Total_Marks(Mark_List):

    Total = sum(Mark_List)
    return Total


def Average(Mark_List):

    Avg = Total_Marks(Mark_List) / len(Mark_List)
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


def Result(Mark_List):

    if Average(Mark_List) >= 50:
        result = "Pass"
    else:
        result = "Fail"

    return result


# Printing 1

print("--Welcome To Student Result Calculator--")
print("----------------------------------------")

# Input 1

Student_Name = input("Enter Your Name : ")
Mark_List = []

# While loop

i = 1
while i <= 3:
    try:
        Subject_Mark = float(input(f"Enter Your Subject {i} Marks : "))
        if 0 <= Subject_Mark <= 100:
            Mark_List.append(Subject_Mark)
            i += 1
        else:
            print("Marks should be between 0 - 100")
    except ValueError:
        print("Please Enter Correct Value!!!")

# Printing 2

print("----------------------------------------")

print(f"\nHello {Student_Name},")
print("-------This is Your Result Summary------")

print(f"\nTotal\t= {Total_Marks(Mark_List)}")
print(f"Average\t= {Average(Mark_List):.2f}")

# For loop

print("\nGrades :")
count = 1
for mark in Mark_List:
    Grade_Result = Grade(mark)
    print(f"\tSubject {count} = {Grade_Result}")
    count += 1

print(f"\nResult\t= {Result(Mark_List)}")

print("---------------Thank You----------------")
