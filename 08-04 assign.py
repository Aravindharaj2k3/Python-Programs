'''1) names=['KISHORE','harish','ganesh','abdul','STEVENS','vekat','PANKAJ','SUMA']
convert all the lower case names to uppercase
final details should be stored in names_upper list
use lambda with map
hint: check on using islower() of str

names = ['KISHORE', 'harish', 'ganesh', 'abdul', 'STEVENS', 'vekat', 'PANKAJ', 'SUMA']

names_upper = list(map(lambda x: x.upper()
if x.islower()
else x, names))
print(names_upper)

2) generate some 50 random numbers in the range of 1 to 500
   store it in list
   find the sum of all numbers in the range of 200 to 300
   find the avg of such numbers, find the highest, lowest (in those range 200 to 300)
   find thesum of all numbers in the range of 200 to 300
   find the avg of all the numbers NOT in the range leaving first 2 numbers
08-04 assign.py '''

import random
numbers=[random.randint(1,499) for _ in range(50)]
find_sum=sum( num for num in numbers if 200 <= num <=300)
avg_find=sum(numbers)/len(numbers) if numbers else none
max_range=max(numbers)if numbers else none
min_range=min(numbers) if numbers else none
avg_not=[num for num in numbers if num  < 200 or num > 300]
print('50 random numbers in the range of 1 to 500',numbers)
print('avg of such numbers',avg_find)
print('sum of all numbers in the range of 200 to 300',find_sum)
print('highest number',max_range)
print('lowlest number',min_range)
print('sum of all numbers in the range of 200 to 300',avg_not)


'''3)generate some 100 random numbers in the range of 1 to 9999
   create list of all THREE digit random numbers
   create list of all ONE digit random numbers
   all the SINGLE digit number - tripple them
   all the TWO digit number - double them
import random
numbers = [random.randint(1,9999) for _ in range(100)]
three_digit=[num for num in numbers if 100 <= num <=999]
two_digit=[ num for num in numbers if num<10]
tripple= [(num * 3) if num < 10 else (num * 2) for num  in numbers]
print(three_digit)
print(two_digit)
print(tripple)

4) in question 3 after the generation of the numbers
   ignore the FIRST 10 number and last 5 numbers
   then do the same activity as in QS 3

import random
numbers=[random.randint(1,50) for _ in range(50)]
first_number=10
last_number=-5
numbers=numbers[first_number:last_number]
sum_of_number=sum(numbers)
print(' ignore the FIRST 10 number and last 5 numbers',numbers)'''

   

