# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def home():
#     return {
#         "message": "Hello! I am learning AI with Python.",
#         "name": "Pintu Kumar Sah",
#         "role": "Java Developer",
#         "goal": "AI Engineer"
#     }

from fastapi import FastAPI

app = FastAPI()


# @app.get("/")
# def home():
#     return {
#         "message": "Welcome to AI Journey",
#         "status": "Running"
#     }


# @app.get("/user")
# def user(name: str, age: int):
#     return {
#         "name": name,
#         "age": age,
#         "message": f"Hello {name}, you are {age} years old."
#     }


# @app.get("/check-age")
# def check_age(age: int):

#     if age >= 18:
#         message = "You are eligible to vote"
#     else:
#         message = "You are not eligible to vote"

#     return {
#         "age": age,
#         "message": message
#     }


@app.get("/employee-details")
def employee_details(
    name: str,
    age: int,
    salary: float,
    experience: int
):

    annual_salary = salary * 12

    if experience >= 5:
        level = "Senior Developer"
    elif experience >= 3:
        level = "Mid-Level Developer"
    else:
        level = "Junior Developer"

    return {
        "name": name,
        "age": age,
        "monthly_salary": salary,
        "annual_salary": annual_salary,
        "experience": experience,
        "level": level
    }