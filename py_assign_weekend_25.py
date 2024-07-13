'''1)create a class MyDate with day,month, year
have a 3 arg constructor assign data
write a method to check whether the date is valid or not

class MyDate:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year

    def valied_date(self):
        #first of all month between
        if not 1 <= self.month <=12:
            return False

        #validate of months in 31 days
        if self.month in [1,3,5,7,8,10,12]:
            return 1 <= self.day <= 31
        #validate of months in 30days
        elif self.month in [2,4,6,9,11]:
            return 1 <= self.day <= 30
        elif self.month ==2:

            #leap year validation
            if self.year %4 ==0:
                if self.year %100 ==0:
                    if self.year %400 ==0:
                        return 1<= self.day <=29
                    else:
                        return 1<= self.day <=28
                else:
                 return 1<= self.day <=29
            else:
              return 1<= self.day <=28

        return False

date1 = MyDate (29,2,2022)
print(date1.valied_date()) #true value

date2 = MyDate (29,2,2021)
print(date2.valied_date()) # falase value
'''

''' 2)create RIGHT classes and methods to solve the below
    company decides to shortlist candidate who has NOT less than 5 years of experince
    and ready to work from office
    he should have atleast two of the given below skills
    SQL,Python, Java, PowerBI,Excel,Javascrip
    and mandatory MUST have one of these skill known: Mongo,Casandra,Redis,Cosmos
    last salary drawn is not less than 6.5 lakhs per annum and salary expectation
    is less than 9L
    must have either MCA or BE degree only

    output ways
    
    output should be either
    shorlisted for the interview
    not shortlisted with reason XXXX


class Employe:
    def __init__(self, experience, office_ready, skills, last_salary, salary_expectation, degree):
        self.experience = experience
        self.office_ready = office_ready
        self.skills = skills
        self.last_salary = last_salary
        self.salary_expectation = salary_expectation
        self.degree = degree

    def shortlisted(self):
        if self.Experince() and \
           self.Ready_work_from_home() and \
           self.Salary_exceptaion() and \
           self.Below_skills() and \
           self.degree_validate():
            return True, "Shortlisted for interview"
        else:
            reasons = []
            if not self.Experince():
                reasons.append("Insufficient experience")
            if not self.Ready_work_from_home():
                reasons.append("Not ready to work from office")
            if not self.Salary_exceptaion():
                reasons.append("Salary expectations not met")
            if not self.Below_skills():
                reasons.append("Insufficient skills")
            if not self.degree_validate():
                reasons.append("Invalid degree qualification")
            return False, "Not shortlisted for interview: " + ', '.join(reasons)

    def Experince(self):
        return self.experience >= 5
    
    def Ready_work_from_home(self):
        return self.office_ready

    def Below_skills(self):
        required_skills = {'Sql', 'pyhton', 'java', 'powerbi', 'excel', 'javascript'}
        mandatory_skills = {'mongo', 'casandra', 'redis', 'cosmos'}
        return len(required_skills.intersection(self.skills)) >= 2 and mandatory_skills.intersection(self.skills)

    def Salary_exceptaion(self):
        return self.last_salary >= 6.5 and self.salary_expectation < 9

    def degree_validate(self):
        return self.degree in ['MCA', 'BE']


candidate1 = Employe(6, True, {'sql', 'python', 'mongo'}, 7.5, 8, 'MCA')
print(candidate1.shortlisted())

candidate2 = Employe(3, False, {'java', 'powerbi', 'excel', 'cosmos'}, 5.0,5.5 , 'BSC')
print(candidate2.shortlisted())

 4)write a class called BatterChargerCheck
   when the battery charge is following display the color code
   80 to 100   green color
   60 to 79    blue color
   45 to 59    orange color
   25 to 44    yello color 
   25 and less red color 
   (but above 0)
   so assume that the battery_charge is assigned with value 74
   if the value assigned is above 100 then raise IllegalBatteryValueException
   if the value assigned is negative then raise IllegalBatteryValueException'''


class IllegalBatteryValueException(Exception):
    pass

class BatteryCheck:
    def __init__(self, battery_charge):
        if battery_charge < 0:
            raise IllegalBatteryValueException("Battery charge value cannot be negative")
        elif battery_charge > 100:
            raise IllegalBatteryValueException("Battery charge value cannot be greater than 100")
        self.battery_charge = battery_charge

    def battery_color(self):
        if self.battery_charge >= 80:
            return "green"
        elif self.battery_charge >= 60:
            return "blue"
        elif self.battery_charge >= 45:
            return "orange"
        elif self.battery_charge >= 25:
            return "yellow"
        else:
            return "red"

# Example usage:
try:
    checker = BatteryCheck(74)
    print("Color:", checker.battery_color())  
except IllegalBatteryValueException as e:
    print("Error:", e)
    
try:
    checker =BatteryCheck(-4)
    print("color:",checker.battery_color())
except IllegalBatteryValueException as a:
    print("Error",a)
    
