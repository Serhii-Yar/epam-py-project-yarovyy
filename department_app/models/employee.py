import uuid

from department_app import db


class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Integer)
    uuid = db.Column(db.String(36), unique=True)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))

    def __init__(self, name, birthdate, salary=0, department=None):
        self.name = name
        self.birthdate = birthdate
        self.salary = salary
        self.uuid = str(uuid.uuid4())
        self.department = department

    def __repr__(self):
        return f'Employee({self.name}, {self.birthdate}, {self.salary})'
