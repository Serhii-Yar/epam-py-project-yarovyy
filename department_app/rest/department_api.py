from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.orm import selectinload

from department_app.schema.department_schema import DepartmentSchema
from department_app.service.department_service import DepartmentService


class DepartmentApiSetup(Resource):
    schema = DepartmentSchema()
    service = DepartmentService()


class DepartmentListApi(DepartmentApiSetup):
    def get(self):
        departments = self.service.get_departments(strat=selectinload)
        return self.schema.dump(departments, many=True), 200

    def post(self):
        try:
            department = self.service.add_department(self.schema, request.json)
        except ValidationError as error:
            return error.messages, 400
        return self.schema.dump(department), 201


class DepartmentApi(DepartmentApiSetup):
    NOT_FOUND_ERROR = 'Department not found'
    NO_CONTENT_ERROR = ''

    def get(self, uuid: str):
        try:
            department = self.service.get_department(uuid)
        except ValueError:
            return self.NOT_FOUND_ERROR, 404
        return self.schema.dump(department), 200

    def put(self, uuid):
        try:
            department = self.service.update_department(
                self.schema, uuid, request.json
            )
        except ValidationError as error:
            return error.messages, 400
        except ValueError:
            return self.NOT_FOUND_ERROR, 404
        return self.schema.dump(department), 200

    def delete(self, uuid):
        try:
            self.service.delete_department(uuid)
        except ValueError:
            return self.NOT_FOUND_ERROR, 404
        return self.NO_CONTENT_ERROR, 204


