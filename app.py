from fastapi import FastAPI

app = FastAPI()

employees = [
    {"id": 1, "name": "Suhail", "role": "DevOps Engineer"},
    {"id": 2, "name": "Ahmed", "role": "Linux Administrator"}
]

@app.get("/")
def home():
    return {"message": "Employee Service Running"}

@app.get("/employees")
def get_employees():
    return employees

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee

    return {"error": "Employee not found"}
