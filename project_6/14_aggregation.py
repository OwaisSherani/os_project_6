class Employee:
    def __init__(self, emp_id, emp_name):
        self.emp_id = emp_id
        self.emp_name = emp_name
    
    def __str__(self):
        return f"Employee ID: {self.emp_id} : Employee Name: {self.emp_name}"

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []  # Aggreation list to hold employee objects

    def add_employee(self, emp):
        if isinstance(emp, Employee):
            self.employees.append(emp)
        else:
            raise TypeError ("Invalid employee object.")
    
    def list_employees(self):
        print(f"Department: {self.dept_name}")
        for emp in self.employees:
            print(f" - {emp}")

# Example Usage
emp1 = Employee(101, "Owais")
emp2 = Employee(102, "Ali")  
emp3 = Employee(103, "Sara")

dept = Department("Production")

dept.add_employee(emp1)
dept.add_employee(emp2) 
dept.add_employee(emp3)

dept.list_employees()



   