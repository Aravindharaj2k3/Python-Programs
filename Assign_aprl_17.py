'''class Employ:
    def __init__(self, emp_id, emp_name):
        self.emp_id = emp_id
        self.emp_name = emp_name

class EmpDptDsg(Employ):
    def __init__(self, emp_id, emp_name, designation, department):
        super().__init__(emp_id, emp_name)
        self.designation = designation
        self.department = department

e1 = EmpDptDsg(emp_id=1000, emp_name='Vijay', designation='Manager', department='Sales')
print(e1.emp_id)  # Accessing emp_id attribute of e1

'''

class Employ:
    def __init__(self,emp_id,emp_name):
        self.emp_id = emp_id
        self.emp_name = emp_name

class EmpDptDsg(Employ):
    def __init__(self,emp_id,emp_name,designation,department):
        super().__init__(emp_id,emp_name)
        self.designation = designation
        self.department = department

e1 = EmpDptDsg(emp_id = 1000,emp_name = 'Vijay',designation= 'Manager', department = 'Sales')
print("Employe_id is:",e1.emp_id)
print('Employe_name is:',e1.emp_name)
print('Employe_designation is:',e1.designation)
print('Employe_department is:',e1.department)

