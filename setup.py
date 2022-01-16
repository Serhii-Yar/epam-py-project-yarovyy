from setuptools import setup, find_packages

setup(
    name='department app',
    version='1.0',
    author='Serhii Yarovyi',
    author_email='yarovyy.s@gmail.com',
    description='',
    url='https://github.com/Serhii-Yar/epam-py-project-yarovyy',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==2.0.2',
        'Flask-Classy==0.6.10',
        'Flask-Migrate==3.1.0',
        'Flask-SQLAlchemy==2.5.1',
        'flask-restful==0.3.9',
        'marshmallow-sqlalchemy==0.27.0',
        'mysql-connector-python==8.0.27'
    ]
)
