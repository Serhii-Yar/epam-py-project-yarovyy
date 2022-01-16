import os

from dotenv import load_dotenv
load_dotenv()

user = os.environ.get('MYSQL_USER')
password = os.environ.get('MYSQL_PASSWORD')
host = os.environ.get('MYSQL_HOST')
port = os.environ.get('MYSQL_PORT')
database = os.environ.get('MYSQL_DATABASE')


class Config:
    DEBUG = True
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{user}:{password}' \
                              f'@{host}:{port}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False