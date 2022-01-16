# epam-py-project-yarovyy

### Installation process:
- ##### Set up python virtual environment:
```
virtualenv venv
source env/bin/activate
```

- ### Install the requirements:
```
pip install -r requirements.txt
```
- ### Set the following environment variables:

```
MYSQL_USER=<your_mysql_user>
MYSQL_PASSWORD=<your_mysql_user_password>
MYSQL_HOST=<your_mysql_host>
MYSQL_PORT=<your_mysql_port>
MYSQL_DATABASE=<your_mysql_database_name>
```

- ### Run migrations to create database infrastructure:
```
flask db init
```

- ### Run the project locally:
```
python -m flask run
```

### Used web addresses:

- ##### For Web Service:
```
localhost:5000/api/departments
localhost:5000/api/department/<uuid>

localhost:5000/api/employees
localhost:5000/api/employees/search/date=<YYYY-MM-DD>
localhost:5000/api/employees/search/start_date=<YYYY-MM-DD>&end_date=<YYYY-MM-DD>
localhost:5000/api/employee/<uuid>
```

##### SwaggerUI with endpoints:
```
localhost:5000/swagger
```

- ##### For Web Application:
```
localhost:5000/

localhost:5000/departments
localhost:5000/department/add
localhost:5000/department/edit
localhost:5000/department/edit/<uuid>
localhost:5000/department/delete
localhost:5000/department/delete/<uuid>

localhost:5000/employees
localhost:5000/employee/add
localhost:5000/employee/edit
localhost:5000/employee/edit/<uuid>
localhost:5000/employee/delete
localhost:5000/employee/delete/<uuid>
```