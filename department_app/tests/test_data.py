# pylint: disable=missing-function-docstring, missing-module-docstring, disable=missing-class-docstring
from datetime import date

from department_app.models.department import Department
from department_app.models.employee import Employee

department_1 = Department('Test Dep 1')
department_2 = Department('Test Dep 2')

employee_1 = Employee('Test Employee 1', date(1996, 5, 12), 2000)
employee_2 = Employee('Test Employee 2', date(1996, 5, 12), 2100)
employee_3 = Employee('Test Employee 3', date(1989, 11, 30), 1800)
employee_4 = Employee('Test Employee 4', date(2000, 7, 14), 1600)
employee_5 = Employee('Test Employee 5', date(1998, 3, 25), 1600)

department_1.employees = [employee_1, employee_2, employee_3]
department_2.employees = [employee_4, employee_5]


def employee_to_json(employee, nested=True):
    result = {
        'birthdate': str(employee.birthdate),
        'name': employee.name,
        'salary': employee.salary,
        'uuid': employee.uuid
    }

    if nested:
        result['department'] = department_to_json(
            employee.department, nested=False
        )

    return result


def department_to_json(department, nested=True):
    total_salary = sum([employee.salary for employee in department.employees])
    result = {
        'name': department.name,
        'uuid': department.uuid,
        'size': len(department.employees),
        'total_salary': total_salary,
        'average_salary': total_salary / len(department.employees)
    }

    if nested:
        result['employees'] = [
            employee_to_json(e, nested=False) for e in department.employees
        ]

    return result
