from department_app import app

from . import index_view
from . import employee_view
from . import department_view


def init_views():
    employee_view.EmployeeView.register(app)
    department_view.DepartmentView.register(app)
    index_view.HomepageView.register(app)
