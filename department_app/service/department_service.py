from sqlalchemy.orm import lazyload

from department_app import db
from department_app.models.department import Department
from department_app.service.strategy_service import StrategiesService


class DepartmentService(StrategiesService):
    @classmethod
    def get_departments(cls, strat=lazyload):
        cls._check_strat(strat)

        return db.session.query(Department)\
            .options(strat(Department.employees)).all()

    @staticmethod
    def get_department(uuid):
        department = db.session.query(Department)\
            .filter_by(uuid=uuid).first()
        if department is None:
            raise ValueError('Invalid department uuid')
        return department

    @staticmethod
    def get_department_by_name(name):
        return db.session.query(Department)\
            .filter_by(name=name).first()

    @staticmethod
    def add_department(schema, department_json):
        department = schema.load(department_json, session=db.session)
        db.session.add(department)
        db.session.commit()
        return department

    @classmethod
    def update_department(cls, schema, uuid, department_json):
        department = cls.get_department(uuid)
        if department is None:
            raise ValueError('Invalid department uuid')
        department = schema.load(department_json, session=db.session, instance=department)
        db.session.add(department)
        db.session.commit()
        return department

    @classmethod
    def delete_department(cls, uuid):
        department = cls.get_department(uuid)
        if department is None:
            raise ValueError('Invalid department uuid')
        db.session.delete(department)
        db.session.commit()
