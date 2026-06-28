# Q-1 
def analyze_string(s):
    print("Length of string:", len(s))

    print("Reversed string:", s[::-1])

    vowels = "aeiou"
    count = 0

    for ch in s.lower():
        if ch in vowels:
            count += 1

    print("Number of vowels:", count)

    print("\nCharacter with Positive and Negative Index:")
    for i in range(len(s)):
        print(f"Character: {s[i]}, Positive Index: {i}, Negative Index: {i - len(s)}")

text = input("Enter a string: ")

if text == "":
    print("Empty string is not allowed.")
else:
    analyze_string(text)



#Q-2
def manage_marks():
    marks = []
    print("Enter marks for 5 subjects:")

    while len(marks) < 5:
        try:
            mark = float(input(f"Enter marks for Subject {len(marks) + 1}: "))
            marks.append(mark)
        except ValueError:
            print("Invalid input! Please enter numeric marks only.")

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    marks.sort(reverse=True)
    print("\n----- Result -----")
    print("Marks List:", marks)
    print("Average Marks:", average)
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)
    print("Marks in Descending Order:", marks)

manage_marks()


# Q-3
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []
    def add_mark(self, mark):
        try:
            mark = float(mark)
            if mark < 0 or mark > 100:
                raise ValueError("Marks should be between 0 and 100.")

            self.marks_list.append(mark)

        except ValueError as e:
            print("Invalid Input:", e)

    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)

    def display_info(self):
        print("\n----- Student Information -----")
        print("Name      :", self.name)
        print("Roll No   :", self.roll_no)
        print("Marks     :", self.marks_list)
        print("Average   :", self.get_average())

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
student = Student(name, roll_no)
print("\nEnter 5 Subject Marks:")

for i in range(5):
    mark = input(f"Enter mark {i + 1}: ")
    student.add_mark(mark)
student.display_info()


# Q-4
def student_database():
    students = {}

    while True:
        print("\n..... Student Database Menu .....")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                roll = input("Enter Roll Number: ")
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")
                students.update({
                    roll: {
                        "Name": name,
                        "Age": age,
                        "City": city
                    }
                })

                print("Student added successfully!")
            elif choice == 2:
                roll = input("Enter Roll Number to Search: ")

                student = students.get(roll)

                if student:
                    print("\nStudent Found")
                    print("Name :", student["Name"])
                    print("Age  :", student["Age"])
                    print("City :", student["City"])
                else:
                    print("Student not found!")
            elif choice == 3:
                if len(students) == 0:
                    print("No student records available.")
                else:
                    print("\n----- Student Records -----")
                    for roll, details in students.items():
                        print(f"\nRoll Number : {roll}")
                        print("Name :", details["Name"])
                        print("Age  :", details["Age"])
                        print("City :", details["City"])

            elif choice == 4:
                print("Exiting Student Database...")
                break

            else:
                print("Invalid choice! Please enter 1 to 4.")
        except ValueError:
            print("Invalid input! Please enter numeric values where required.")

student_database()


# Q-5
import random
import math

s = set()

try:
    for i in range(10):
        n = int(input("Enter number: "))
        s.add(n)
    t = tuple(s)

    print("Set:", s)
    print("Tuple:", t)
    if len(t) >= 3:
        print("Random Numbers:", random.sample(t, 3))
    else:
        print("Less than 3 unique numbers.")
    total = sum(t)
    print("Sum:", total)
    print("Square Root:", math.sqrt(total))

except ValueError:
    print("Invalid input! Please enter numbers only.")

except Exception as e:
    print("Error:", e)


    # Q-6
    square = lambda x: x * x

try:
    squares = []
    for i in range(1, 21):
        squares.append(square(i))

    print("Squares:", squares)

    print("Even Squares:")
    for i in squares:
        if i % 2 == 0:
            print(i)

except Exception as e:
    print("Error:", e)

    # Q-7
    class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.details = (department, salary)   

    def show_details(self):
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Department  :", self.details[0])
        print("Salary      :", self.details[1])
        print()

employees = {}
for i in range(3):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))
    employees[emp_id] = Employee(emp_id, name, department, salary)
print("\nEmployee Details")
for emp in employees.values():
    emp.show_details()


    # Q-8
    import math

try:
    sentence = input("Enter a sentence: ")
    words = set(sentence.split())
    print("Unique Words:", sorted(words))
    count = len(words)
    print("Count^2 =", math.pow(count, 2))

except Exception as e:
    print("Error:", e)


    # Q-9
    import math
import random
history = {}
def basic():
    try:
        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        ch = int(input("Enter Choice: "))

        if ch == 1:
            result = a + b
        elif ch == 2:
            result = a - b
        elif ch == 3:
            result = a * b
        elif ch == 4:
            result = a / b
        else:
            print("Invalid Choice")
            return

        print("Result =", result)

        time = input("Enter Timestamp: ")
        history[time] = result

    except ValueError:
        print("Invalid Input!")
    except ZeroDivisionError:
        print("Cannot Divide by Zero!")

def scientific():
    try:
        n = float(input("Enter Number: "))

        print("Square Root =", math.sqrt(n))
        print("Power =", math.pow(n, 2))

        time = input("Enter Timestamp: ")
        history[time] = math.pow(n, 2)

    except Exception as e:
        print("Error:", e)

def random_number():
    num = random.randint(1, 100)
    print("Random Number =", num)

    time = input("Enter Timestamp: ")
    history[time] = num

def view_history():
    if len(history) == 0:
        print("No History Available")
    else:
        print("\nHistory")
        for key, value in history.items():
            print(key, ":", value)

while True:
    print("\n===== Smart Calculator =====")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculation")
    print("3. Generate Random Number")
    print("4. View History")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        basic()

    elif choice == 2:
        scientific()

    elif choice == 3:
        random_number()

    elif choice == 4:
        view_history()

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")

        

