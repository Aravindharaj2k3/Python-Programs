#1. The type of values in first sowing for logistice values?

def aravind(emp):
    print('Employe details',emp)
    for i,k in emp.items():
        print(i,k)
        print() 
def raju(emp):
    dept = 'IT'
    emp_logic = {i: k for i,k in emp.items() if k[1].upper() == dept}
    return emp_logic


print('start the main block')
emp = {101:['Aravindharaj','sales'],102:['Rajubjhai','It'],103:['vishal seker','It'],
       345:['Waseem akram','Logistics'],
       5858:['Rajivee kochi','Logistics']}
aravind(emp)
emp_logic = raju(emp)
aravind(emp_logic)
print('End the main block')

