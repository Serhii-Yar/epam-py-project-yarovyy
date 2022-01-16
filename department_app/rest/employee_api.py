from datetime import datetime

from flask import request
from flask_restful import Resource, reqparse
from marshmallow import ValidationError
from sqlalchemy.orm import selectinload

from department_app.schema.employee_schema import EmployeeSchema
from department_app.service.employee_service import EmployeeService


def get_date(date_str, date_format='%Y-%m-%d'):
    """
    Returns formatted date string or None
    :param date_str:
    :param date_format:
    :return:
    """
    try:
        return datetime.strptime(date_str, date_format).date()
    except (ValueError, TypeError):
        return None


class EmployeeApiSetup(Resource):
    schema = EmployeeSchema()
    service = EmployeeService()


class EmployeeListApi(EmployeeApiSetup):
    def get(self):
        employees = self.service.get_employees(strat=selectinload)
        return self.schema.dump(employees, many=True), 200

    def post(self):
        try:
            employee = self.service.add_employee(self.schema, request.json)
        except ValidationError as error:
            return error.messages, 400
        return self.schema.dump(employee), 201


class EmployeeApi(EmployeeApiSetup):
    NOT_FOUND_ERROR = 'Employee not found'
    NO_CONTENT_ERROR = ''

    def get(self, uuid: str):
        try:
            employee = self.service.get_employee(uuid)
        except ValueError:
            return self.NOT_FOUND_ERROR, 404
        return self.schema.dump(employee), 200

    def put(self, uuid: str):
        try:
            employee = self.service.update_employee(
                self.schema, uuid, request.json
            )
        except ValidationError as error:
            return error.messages, 400
        except ValueError:
            return self.NOT_FOUND_ERROR, 404
        return self.schema.dump(employee), 200

    def delete(self, uuid: str):
        try:
            self.service.delete_employee(uuid)
        except ValueError:
            return self.NOT_FOUND_ERROR, 404
        return self.NO_CONTENT_ERROR, 204


class EmployeeDateSearchApi(EmployeeApiSetup):
    parser = reqparse.RequestParser()
    parser.add_argument('date')
    parser.add_argument('start_date')
    parser.add_argument('end_date')

    BAD_DATE_ERROR = 'Incorrect date format'

    def get(self):
        args = self.parser.parse_args()
        date = get_date(args['date'])
        start_date = get_date(args['start_date'])
        end_date = get_date(args['end_date'])

        if date:
            employees = self.service\
                .get_employees_by_date(date, strategy=selectinload)
        elif start_date and end_date:
            employees = self.service\
                .get_employees_between_dates(start_date, end_date, strategy=selectinload)
        else:
            return self.BAD_DATE_ERROR, 400

        return self.schema.dump(employees, many=True), 200

