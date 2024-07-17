#Write a program that takes an integer input from the user and prints whether the number is odd or even.

int_var = int(input('Enter the number'))
if int_var %2==0:
    print(int_var,'Is a even number')
else:
    print(int_var,'Is a Odd number')

#Write a program that takes a score (0-100) as input and prints the grade based on the following criteria:
#90-100: A
#80-89: B
#70-79: C
#60-69: D
#Below 60: F

var = int(input('Enter a marks'))
if var >=90 <=100:
    print('Grade is A')
elif var >=80 <=89:
    print('Grade is B')
elif var >=70 <=79:
    print('Grade is c')
elif var >=60 <=69:
    print('Grade is c')
else:
    print('fail')


#Write a program to check if a given year is a leap year. A year is a leap year if it is divisible by 4, but not divisible by 100 unless it is also divisible by 400.

yr = int(input("Enter a year:"))
if yr %4==0:
    if yr % 100 !=0 or yr % 400 ==0:
        print(f'{yr},Is a leap year')
    else:
        print(f'{yr},Is not a leap year')
else:
     print(f'{yr},Is not a leap year')

#Write a program that takes three numbers from the user and prints the largest one.
    
dic = {124,544,533}
mx_value = max(dic)
mi_value = min(dic)
print('max value',mx_value)
print('min value',mi_value)


#Factorial number

def fact(n):
    if n ==1:
        return n
    else:
        return n*fact(n-1)
print('Is a Factorial number',fact(5))
'''
#Write a program that takes a string input from the user and counts the number of vowels in the string.
'''
srt = str(input('Enter the string value:'))
vow=['a','e','i','o','u','s']
count =0
for i in srt:
    if i in vow:
       count+=1
print('count the values vowels ',count)

#1String Reversal

#Write a program that takes a string input from the user and prints the reversed string.

var  = str(input('Enter a number:'))
var1 = var[::-1]
print('Reverse the value:',var1)

#Dictionary Operations
#Write a program to create a dictionary with key-value pairs and perform the following operations:
#1.Add a new key-value pair.

set1={'Aravind','Raju'}
add_data = set1.add({'Aravikuamr'})
print("Add the elements",add_data)
'''

#Update an existing key with a new value.

'''
set1={'name':'Aravind','age':'23'}
update_value = set1['age'] ='34'
print(set1)

#Delete a key from the dictionary.

value = [{'Cars_name': 'Adudi','Price':'45k'},
{'Cars_name': 'Mahi','Price':'58k'}]
del_value =value.pop("Cars_name")
print(del_value)

#Print the dictionary after each operation.

#Tuple Operations

#item a program to create a tuple with at least 5 elements and perform the following operations:
#1Access an element by its index.

var =('Aravindharaj','rajubhai','raju','kumar','bhai')
var_index = var.index('raju')
print('var_index vales is there',var_index)


#3Find the length of the tuple.
values =('aravidn','raju','brother')
count = 0
for i in values:
    count +=1
print('strig of count value is:',count)


#Set Operations

#multiplaction


numm =8
for i in range(1,11):
    print(numm,'*',i,'=',numm*i)


#Write a program to create two sets and perform the following operations:
#Union of the sets
#1Intersection of the sets.
#2Difference between the sets.
#3Print the result of each operation.


set1 = {1,2,3,4,5,6}
set2 = {45,6,7,5,3,2}
set_addition = (set1.union(set2))
print('Addition value',set_addition)
set_inter = set1.intersection(set2)
print('Intersection value',set_inter)
set_diif = set1.difference(set2)
print('differnce value',set_diif)



