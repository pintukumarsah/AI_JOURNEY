name = input("Enter employee name: ")
age = int(input("Enter age: "))
salary = float(input("Enter monthly salary: "))
experience = int(input("Enter experience in years: "))

annual_salary = salary * 12

print("\n----- Employee Details -----")
print(f"Name       : {name}")
print(f"Age        : {age}")
print(f"Salary     : {salary}")
print(f"Experience : {experience} years")
print(f"Annual     : {annual_salary}")