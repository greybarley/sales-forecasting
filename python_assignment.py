class Employee:
    def _init_(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def _init_(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, age):
        result = [emp for emp in self.employees if emp.age == age]
        return result

    def search_by_name(self, name):
        result = [emp for emp in self.employees if emp.name == name]
        return result

    def search_by_salary(self, operator, salary):
        if operator == '<':
            result = [emp for emp in self.employees if emp.salary < salary]
        elif operator == '<=':
            result = [emp for emp in self.employees if emp.salary <= salary]
        elif operator == '>':
            result = [emp for emp in self.employees if emp.salary > salary]
        elif operator == '>=':
            result = [emp for emp in self.employees if emp.salary >= salary]
        else:
            result = []
        return result
    
    def display_result(self, result):
        if not result:
            print("No matching records found.")
        else:
            print("EmployeeID Name\tAge\tSalary (PM)")
            for emp in result:
                print(f"{emp.employee_id}\t{emp.name}\t{emp.age}\t{emp.salary}")

if _name_ == "_main_":
    table = EmployeeTable()

    # Add employees to the table
    table.add_employee(Employee("161E90", "Raman", 41, 56000))
    table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    table.add_employee(Employee("171E20", "Tejas", 30, 55000))
    table.add_employee(Employee("171G30", "Ajay", 45, 44000))

    search_option = int(input("Choose search parameter:\n1. Age\n2. Name\n3. Salary\n"))

    if search_option == 1:
        age = int(input("Enter age to search: "))
        result = table.search_by_age(age)
    elif search_option == 2:
        name = input("Enter name to search: ")
        result = table.search_by_name(name)
    elif search_option == 3:
        operator = input("Enter salary operator (<, <=, >, >=): ")
        salary = float(input("Enter salary to compare: "))
        result = table.search_by_salary(operator, salary)
    else:
        print("Invalid option")
        result = []

    table.display_result(result)