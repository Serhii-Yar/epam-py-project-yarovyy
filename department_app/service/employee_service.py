from sqlalchemy import and_
from sqlalchemy.orm import lazyload

from department_app import db
from department_app.models.employee import Employee
from department_app.service.strategy_service import StrategiesService


class EmployeeService(StrategiesService):
    @classmethod
    def get_employees(cls, strat=lazyload):
        cls._check_strat(strat)

        return db.session.query(Employee)\
            .options(strat(Employee.department)).all()

    @staticmethod
    def get_employee(uuid):
        employee = db.session.query(Employee)\
            .filter_by(uuid=uuid).first()
        if employee is None:
            raise ValueError('Invalid employee id')
        return employee

    @classmethod
    def get_employees_by_date(cls, date, strategy=lazyload):
        cls._check_strat(strategy)
        employees = db.session.query(Employee)\
            .options(strategy(Employee.department))\
            .filter_by(birthdate=date).all()
        return employees

    @staticmethod
    def add_employee(schema, employee_json):
        employee = schema.load(employee_json, session=db.session)
        db.session.add(employee)
        db.session.commit()
        return employee

    @classmethod
    def update_employee(cls, schema, uuid, employee_json):
        employee = cls.get_employee(uuid)
        if employee is None:
            raise ValueError('Invalid employee uuid')
        employee = schema.load(employee_json, session=db.session, instance=employee)
        db.session.add(employee)
        db.session.commit()
        return employee

    @classmethod
    def delete_employee(cls, uuid):
        employee = cls.get_employee(uuid)
        if employee is None:
            raise ValueError('Invalid employee uuid')
        db.session.delete(employee)
        db.session.commit()

    @classmethod
    def get_employees_between_dates(cls, start_date, end_date, strategy=lazyload):
        cls._check_strat(strategy)

        employees = db.session.query(Employee)\
            .options(strategy(Employee.department))\
            .filter(and_(
                Employee.birthdate > start_date,
                Employee.birthdate < end_date))\
            .all()
        return employees
