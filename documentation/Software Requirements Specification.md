# Department app
### Vision
“Department app” is a web application which allows users to record and review information about departments and their employees.
Application should include:
- Storing departments and employees in a database;
- Displaying list of departments;
- Means to update and modify the list of departments;
- Displaying list of employees;
- Means to update and modify the list of employees;
- Filtering by size for departments;
- Filtering by hire date for employees;

### Homepage

***Main scenario:***
- User selects *"Home"* menu item
- Application homepage is displayed as follows

![Index](../department_app/static/documentation_pics/Index.png)
### 1.Departments
#### 1.1.Display list of departments
The mode is designed to view the list of departments and information regarding every department, 
***Main scenario:***
- User selects item “Departments” in navbar;
- Application displays list of departments.

List contains following columns:
- Number - unique identifier of the department
- Name - name of the department
- Size - amount of employees in the department
- Salary - total amount of salaries paid in department
- Avg_Salary - average salary per department
Aggregate function: Salary = sum(Salary of employee) where Department = current department
![Departments](../department_app/static/documentation_pics/Departments.png)
#### 1.2.Add new department
***Main scenario:***
- User clicks the *"Add new"* button in the departments list view mode
- Application redirects user to the department management page with the "Add 
  department" panel being active
- User enters data and presses the *"Submit"* button
- If entered data is valid, the record is added to the database and message 
  indicating success is displayed
- If error occurs, then error message is displayed

![Add department](../department_app/static/documentation_pics/Add department.png)

**Constraints:**
- Entered name must be unique

#### 1.3.Edit existing department
***Main scenario:***
- User clicks the *"Edit"* button in the departments list view mode
- Application redirects user to the department management page with the "Edit 
  department" panel being active
- User chooses the department, enters data and presses the *"Submit"* button
- If entered data is valid, the corresponding record is updated in the database 
  and message indicating success is displayed
- If error occurs, then error message is displayed

![Edit department](../department_app/static/documentation_pics/Edit department.png)

**Constraints:**
- Entered name must be unique

#### 1.4.Remove existing department
***Main scenario:***
- User clicks the *"Delete"* button in the departments list view mode
- Application redirects user to the department management page with the "Delete 
  department" panel being active
- User chooses the department and presses the *"Delete"* button
- If chosen department is still in the database, the corresponding record is 
  deleted from the database and message indicating success is displayed
- If error occurs, then error message is displayed

![Delete department](../department_app/static/documentation_pics/Delete department.png)

### 2.Employees
#### 2.1.Display list of employees
***Main scenario:***
- User selects item “Employees” in navbar;
- Application displays list of employees.

List contains following columns:
- Number - employee's unique identifier
- Name - full name of the employee
- Salary - employee's salary
- Birthdate - employee's date of birth
- Department - employee's department
![Employees](../department_app/static/documentation_pics/Employees.png)
#### 2.2.Register(add) new employee
***Main scenario:***
- User clicks the *"Add new"* button in the employees list view mode
- Application redirects user to the employee management page with the "Add 
  employee" panel being active
- User chooses the department for the employee, enters data and presses the 
  *"Submit"* button
- If entered data is valid, the record is added to the database and message 
  indicating success is displayed
- If error occurs, then error message is displayed

![Add employee](../department_app/static/documentation_pics/Add employee.png)
#### 2.3.Modify existing employee
***Main scenario:***
 User clicks the *"Edit"* button in the employees list view mode
- Application redirects user to the employee management page with the "Edit 
  employee" panel being active
- User chooses the department and one of its employees, enters data, chooses 
  new department for the employee and presses the *"Submit"* button
- If entered data is valid, the corresponding record is updated in the database 
  and message indicating success is displayed
- If error occurs, then error message is displayed

![Edit employee](../department_app/static/documentation_pics/Edit employee.png)
#### 2.4.Delete existing employee
***Main scenario:***
- User clicks the *"Delete"* button in the employees list view mode
- Application redirects user to the employee management page with the "Delete 
  department" panel being active
- User chooses the department and one of its employees, then presses the 
  *"Delete"* button
- If chosen employee is still in the database, the corresponding record is 
  deleted from the database and message indicating success is displayed
- If error occurs, then error message is displayed

![Delete employee](../department_app/static/documentation_pics/Delete employee.png)
