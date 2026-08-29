# 1. if / elif / else
# 2. Comparison Operators
# 3. Logical Operators
# 4. for loop
# 5. while loop
# 6. range()
# 7. List
# 8. Tuple
# 9. Set
# 10. Dictionary
# 11. Practical Employee API


# age=input("Enter your age: ")
# if int(age ) >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")  


# marks = int(input("Enter your marks: "))

# if marks >= 90:
#     print("A+")
# elif marks >= 80:
#     print("A")
# elif marks >= 70:
#     print("B")
# elif marks >= 60:
#     print("C")
# else:
#     print("Fail")


# name = input("Enter your name: ")
# marks = float(input("Enter your marks: "))

# if marks >= 90:
#     grade = "A+"
# elif marks >= 80:
#     grade = "A"
# elif marks >= 70:
#     grade = "B"
# elif marks >= 60:
#     grade = "C"
# else:
#     grade = "Fail"

# print(f"Name: {name}")
# print(f"Marks: {marks}")
# print(f"Grade: {grade}")


# age = int(input("Enter your age: "))
# salary = float(input("Enter your monthly salary: "))

# if age >= 18 and salary >= 30000:
#     print("Eligible")
# else:
#     print("Not Eligible")

# number = int(input("Enter number: "))

# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# experience = 4
# skill = "Python"

# if experience >= 3 or skill == "Python":
#     print("Shortlisted")
# else:
#     print("Rejected")

# for i in range(1, 6):
#     print(i)

# number = int(input("Enter number: "))

# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")

# i = 1

# while i <= 5:
#     print(i)
#     i += 1


# names = ["Pintu", "Rahul", "Amit", "Ravi"]

# print(names)

# print(names[0])
# print(names[1])

# names = ["Pintu", "Rahul"]

# names.append("Amit")

# print(names)
# names.remove("Rahul")

# names = ["Pintu", "Rahul", "Amit", "Ravi"]

# for name in names:
#     print(name)


# numbers = (10, 20, 30, 40)

# print(numbers)
# print(numbers[0])


# numbers = {10, 20, 30, 20, 10}

# print(numbers)

# employee = {
#     "name": "Pintu",
#     "age": 28,
#     "salary": 50000,
#     "experience": 4
# }

# print(employee["name"])
# print(employee["salary"])
# employee["salary"] = 60000
# employee["city"] = "Delhi"



# employee = {
#     "name": "Pintu",
#     "age": 28,
#     "salary": 50000
# }

# for key, value in employee.items():
#     print(key, ":", value)