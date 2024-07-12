



#3
'''
 given emp = { 100:'Sudha',199:'Ramesh',900:'Ashok',192:'Pankaj',188:'Xavier',672:'Abdul',
                 410:'Vivek',818:'Karthik',755:'Zaheer',500:'Patrick', 210:'Stephen}
   this emp put in main BLOCK
   from there call a method get_name - to which you pass the dict and the empId
   if the ID exists then function returns the name otherwise return 'No such employee'
   similarly write a function add_emp() to which you pass the emp dict,id, name
   if the ID does not exist then add the ID and the name
   for example add_emp(emp,179,'Kiran Kumar') <<<< should be added
   for example add_emp(emp,755,'Deepak Rao') <<<< should NOT be added as 755 already exists in emp
   take care of that
'''

def check_id(emp,id_):
    if id_ in emp:
        return True
    else:
        False


def add_emp(emp,id_,name):
    if check_id(emp,id_):
        print('Id already exist')
    else:
        emp[id_]=name
        return emp
    
emp = { 100:'Sudha',199:'Ramesh',900:'Ashok',192:'Pankaj',188:'Xavier',672:'Abdul',
                 410:'Vivek',818:'Karthik',755:'Zaheer',500:'Patrick', 210:'Stephen'}
print('(Enter - 1) to ckeck for ID')
print('(Enter - 2) to Add new Employee')
inp = int(input('Enter here:'))
if inp == 1:
    i = int(input('Enter id to check:'))
    ret = check_id(emp,i)
    if ret == True:
        print('The user you are lookin for is:', emp.get(i),' at ID', i)
    else:
        print('No such employee')
    
if inp == 2:
    i = int(input('Enter id:'))
    nam =  input('Enter Name:')
    ret = add_emp(emp,i,nam)
    emp = ret
    print(emp)


#4)

'''use lambda to solve this
   convert 'C' temp to 'F' formula is 9/5 x C + 32   here given c1 = 35 find the 'F'
   convert 'F' temp to 'C' formula is 5/9 x (F - 32) here given f1 = 167 find the 'C'
'''
'''
def c_to_f(tempr):
    temp_f = (5/9) * (tempr + 32)
    print( '{0:.2f}'.format(temp_f),' F')

def f_to_c(tempr):
    temp_c = (9/5) * (tempr - 32)
    print('{0:.2f}'.format(temp_c),' C')
    
c1 = 35
print(c1, ' C')
c_to_f(c1)

print()

f1 = 167
print(f1, ' F')
f_to_c(f1)

'''

#5)
'''given cost price = 170 , profit percentage is 12.5
   find the selling price , write it using lambda
'''
'''
cost_price = 170
profit_percentage = 12.5
print('Cost Price: ', cost_price)
print('Profit Percentage: ', profit_percentage)


selling_price = (lambda cp,pp : cp+(cp*pp)/100)
sp = selling_price(cost_price, profit_percentage)
print('Selling Price = ', sp)
'''

#6)
'''
use lambda, if the cost price is less than 200 then profit percentage is 12.5 otherwise
   if is 10.5 , calculate the selling price (hint: use if within lambda)
'''
'''
cost_price_1 = 190
print('Cost Price: ', cost_price_1)

cost_price_2 = 250
print('Cost Price: ', cost_price_2)


selling_price_1 = (lambda cp: cp+(cp*12.5)/100 if cp < 200 else cp+(cp*10.5)/100)
sp_1 = selling_price_1(cost_price_1)
sp_2 = selling_price_1(cost_price_2)

print('Selling Price = ', sp_1,' For Cost Price: ', cost_price_1)
print('Selling Price = ', sp_2,' For Cost Price: ', cost_price_2)
'''

#7) 
'''use filter and lambda to solve this...
   data1 = [190,33,78,119,451,890,5,917,19,80,1119,2119,70,159,1000,210,213,800,120]
   sum all the THREE digit odd number
   print the avg also
   print the highest, lowest
   
'''
'''
data1 = [190,33,78,119,451,890,5,917,19,80,1119,2119,70,159,1000,210,213,800,120]
sum_data1 = sum(filter(lambda i: i>99 and i<1000 and i%2==1, data1))
list_of_3 = list(filter(lambda i: i>99 and i<1000 and i%2==1, data1))
avg_data1 = sum(filter(lambda i: i>99 and i<1000 and i%2==1, data1)) / len(list_of_3)

print('Sum of all 3 digit odd numbers: ', sum_data1)
print('Average of all 3 digit odd numbers: ', '{0:.2f}'.format(avg_data1))
print('Highest of all 3 digit odd numbers: ', max(list_of_3))
print('Lowest of all 3 digit odd numbers: ', min(list_of_3))
'''

#8) 
'''
using the same data1 (in QS 7) use filter and lambda
   find the total of numbers divisible by 5
   find the total of numbers divisible by 5 but for THREE digit number ONLY
   try casting 
      using the set
      using the list
      using the tuple
   hint:::  set(filter(LAMBDA RULE , data1))
            tuple(filter(LAMBDA RULE , data1))
   and so on...
   '''
'''
data1 = [190,33,78,119,451,890,5,917,19,80,1119,2119,70,159,1000,210,213,800,120]
div_5= list(filter(lambda i:  i%5==0, data1))
div_5_3digits = list(filter(lambda i: i>99 and i<1000 and  i%5==0, data1))

print('Number divisible by 5:', div_5)
print('Number divisible by 5 in 3 digits:', div_5_3digits)
'''
'''
#  try casting 

data1 = [190,200,190,33,78,119,451,890,5,917,1,625,19,80,1119,2119,70,159,1000,210,213,800,120,200,625,1]

##      using the set
set_div_5= set(filter(lambda i:  i%5==0, data1))
print('Casting with set Number divisible by 5: ',set_div_5)

##      using the list
list_div_5= list(filter(lambda i:  i%5==0, data1))
print('Casting with list Number divisible by 5: ',list_div_5)

##      using the tuple
tuple_div_5= tuple(filter(lambda i:  i%5==0, data1))
print('Casting with tuple Number divisible by 5: ',tuple_div_5)
'''  


'''
given the article of type A the cost price is 100 rs
                        type B the cost price is 200 rs
   calculate the Selling price if the profit percentage 
   for type A product should be between 8% to 10%
   for type B product should be between 11% to 15%
   selling price = cost price + (cost price x profit percentage)/100
#2
 for the 1) given two list one of type and the other of Profit percentage
   compute the selling price
   prod_type   = ['A','B','A','A','A','B','B','A','B']
   profit_perc = [8.5, 11.5, 9, 10, 9.5, 14.5, 13, 9 , 15]
   it should display the selling price take the formula as given above in QS 1)
'''
'''
def calc_selling_price(pt,pp):
    sp=[]
    for i in range(len(pt)):
        if pt[i] =='A' and (pp >= 8.00 and pp<=10.00):
            sp.append(100+(100*pp)/100)
        if pt[i] == 'B' and pp >= 11.00 and pp<=15.00:
            sp.append(200+(200*pp)/100)  
            return sp


prod_type   = ['A','B',  'A','A','A','B',  'B','A','B']
profit_perc = [8.5, 11.5, 9, 10, 9.5, 14.5, 13, 9 , 15]
print(calc_selling_price(prod_type,profit_perc))
'''

'''
def calc_sp(pt,pp):
    dict_pt_pp[pt] = pp
    for i in range(len(dict_pt_pp))
    if dict_pt_pp
prod_type   = ['A','B',  'A','A','A','B',  'B','A','B']
profit_perc = [8.5, 11.5, 9, 10, 9.5, 14.5, 13, 9 , 15]
'''



