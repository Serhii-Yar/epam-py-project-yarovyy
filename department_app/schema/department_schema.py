from marshmallow import validates_schema, ValidationError, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from department_app.models.department import Department
from department_app.service.department_service import DepartmentService


class DepartmentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Department
        exclude = ['id']
        load_instance = True
        include_fk = True
        dump_only = ('employees',)

    size = fields.Method('calculate_size')
    total_salary = fields.Method('calculate_total_salary')
    average_salary = fields.Method('calculate_average_salary')

    employees = fields.Nested('EmployeeSchema', many=True, exclude=('department',))

    def calculate_size(self, department):
        return len(department.employees)

    def calculate_total_salary(self, department):
        return sum(map(lambda employee: employee.salary, department.employees))

    def calculate_average_salary(self, department):
        try:
            return sum(map(lambda employee: employee.salary, department.employees)) / len(department.employees)
        except ZeroDivisionError:
            return 0

    @validates_schema
    def validate_uniqueness(self, data, **kwargs):
        department = DepartmentService.get_department_by_name(name=data['name'])
        if department is not None:
            raise ValidationError('Non-unique department name')
