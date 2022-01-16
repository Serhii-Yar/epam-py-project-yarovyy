"""
Root package. Needed for initialization.

Subpackages:
- `migrations`: manages database schema
- `models`
- `rest`
-
"""

import logging.config
import os
import sys

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

from flask_restful import Api
from config import Config

TEMPLATES_DIR = 'templates'
MIGRATION_DIR = os.path.join('department_app', 'migrations')

app = Flask(__name__, template_folder=TEMPLATES_DIR)
app.config.from_object(Config)

formatter = logging.Formatter('%(asctime)s %(name)s: %(message)s')

file_handler = logging.FileHandler(filename='app.log', mode='w')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

logger = app.logger
logger.handlers.clear()
app.logger.addHandler(file_handler)
app.logger.addHandler(console_handler)
app.logger.setLevel(logging.DEBUG)

werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.handlers.clear()
werkzeug_logger.addHandler(file_handler)
werkzeug_logger.addHandler(console_handler)
werkzeug_logger.setLevel(logging.DEBUG)

api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db, directory=MIGRATION_DIR)

# Swagger settings
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={'app_name': 'Department app'}
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix='/swagger')

from .rest import init_api
init_api()

from .views import init_views
init_views()

from .models import department, employee
