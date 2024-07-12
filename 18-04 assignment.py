class Employe:
  def __init__(self,eid,ename):
    self.Employe_id = eid
    self.Employe_name = ename

  def emp(self):
      print('employe_id:', self.eid)
      print('employe_id:',self.ename)

class empdpt(Employe):
  def __init__(self,eid,ename,des,dep):
    super().__init__(eid,ename)
    self.E_designation = des
    self.E_department = dep

  def emp(self):
      super().emp()
      print('designation:',self.des)
      print('department:',self.dep)
      
    
employe = [
    empdpt(eid ='10001',ename ='aravind',des ='manger',dep='It'),
    empdpt(eid ='10001',ename ='aravind',des ='manger',dep='It'),
    empdpt(eid ='10001',ename ='aravind',des ='manger',dep='It') ]


for i in employe:
    employe.emp()
   
class Employ:
    def __init__(self, empid, name):
        self.empid = empid
        self.name = name

    def emp_disp(self):
        print("Employee ID:", self.empid)
        print("Name:", self.name)


class EmpDptDsg(Employ):
    def __init__(self, empid, name, designation, department):
        super().__init__(empid, name)
        self.designation = designation
        self.department = department

    def emp_disp(self):
        super().emp_disp()
        print("Designation:", self.designation)
        print("Department:", self.department)


# Creating employees and storing them in a list
employees = [
    EmpDptDsg(empid='E001', name='John Doe', designation='Manager', department='Marketing'),
    EmpDptDsg(empid='E002', name='Jane Smith', designation='Engineer', department='Engineering'),
    EmpDptDsg(empid='E003', name='Alice Johnson', designation='Analyst', department='Finance')
]

# Displaying employee information
for employee in employees:
    print("\nEmployee Details:")
    employee.emp_disp()


