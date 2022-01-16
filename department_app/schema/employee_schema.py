from marshmallow import validates_schema, ValidationError, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from department_app.models.employee import Employee
from department_app.service.department_service import DepartmentService


class DepartmentDeserializer(fields.Nested):
    def __init__(self):
        super().__init__('DepartmentSchema', exclude=('employees',), required=True)

    def _deserialize(self, value, attr, data, partial=None, **kwargs):
        try:
            department_id = data['department']['uuid']
            return DepartmentService.get_department(department_id)
        except KeyError as deserializer_error:
            raise ValidationError('Department missing required field uuid') from deserializer_error


class EmployeeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        exclude = ['id', 'department_id']
        load_instance = True
        include_fk = True
    department = DepartmentDeserializer()
