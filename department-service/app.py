from fastapi import FastAPI, HTTPException
import httpx
import os

app = FastAPI()

EMPLOYEE_URL = os.getenv(
    "EMPLOYEE_SERVICE_URL",
    "http://employee-service:8000"
)

departments = [
    {"id": 1, "name": "IT"},
    {"id": 2, "name": "HR"}
]

@app.get("/")
def home():
    return {"message": "Department Service Running"}

@app.get("/departments")
def get_departments():
    return departments

@app.get("/departments/{department_id}/employees")
async def get_department_employees(department_id: int):

    department = next(
        (d for d in departments if d["id"] == department_id),
        None
    )

    if not department:
        raise HTTPException(status_code=404, detail="Department not found")

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{EMPLOYEE_URL}/employees",
            timeout=5.0
        )

    response.raise_for_status()

    return {
        "department": department,
        "employees": response.json()
    }
