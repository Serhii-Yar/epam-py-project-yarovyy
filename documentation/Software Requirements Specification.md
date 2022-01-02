# Department app
### Vision
“Department app” is a web application which allows users to record and review information about departments, their empoyees and metrics.
Application should include:
-	Storing departments and empoyees in a database;
-	Displaying list of departments;
-	Means to update and modify the list of departments;
-	Displaying list of empoyees;
-	Means to update and modify the list of empoyees;
-	Displaying list of tickets;
-	Means to update and modify the list of tickets;
-	Filtering by size for departments;
-	Filtering by hire date for empoyees;
-	Filtering by priority for tickets;
### 1.Deparments
#### 1.1.Display list of departments
The mode is designed to view the list of departments and information regarding every department, 
***Main scenario:***
- User selects item “Departments” in navbar;
- Application displays list of departments.

List contains following columns:
- Number - unique identifier of the deparment
- Name - name of the department
- Size - amount of employees in the department
- Salary - total amount of salaries payed in department
Aggregate function: Salary = sum(Salary of employee) where Department = current department
***Sort by size:***
#### 1.2.Add new department
***Main scenario:***
***Cancel operation scenario:***
#### 1.3.Edit existing department
***Main scenario:***
***Cancel operation scenario:***
#### 1.4.Remove existing department
***Main scenario:***
***Cancel operation scenario:***
### 2.Employees
#### 2.1.Display list of employees
***Main scenario:***
- User selects item “Employees” in navbar;
- Application displays list of employees.

List contains following columns:
- Number - employee's unique identifier
- Name - full name of the employee
- Salary - employee's salary
- Expirience - time since hire
- Department - employee's deparment
Aggregate function: Expirience = current date - hire date
***Sort by expirience:***
#### 2.2.Register(add) new employee
***Main scenario:***
***Cancel operation scenario:***
#### 2.3.Modify existing employee
***Main scenario:***
***Cancel operation scenario:***
#### 2.4.Delete existing employee
***Main scenario:***
***Cancel operation scenario:***
### 3.Tickets
#### 2.1.Display list of tickets
***Main scenario:***
***Sort by priority:***
#### 2.2.Add new ticket
***Main scenario:***
***Cancel operation scenario:***
#### 2.3.Modify existing ticket
***Main scenario:***
***Cancel operation scenario:***
#### 2.4.Delete existing ticket
***Main scenario:***
***Cancel operation scenario:***
