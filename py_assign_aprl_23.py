'''1) n = 10
   check whether the number is odd or even
   store few of these numbers in the .json file like
   {
     "n1" : [12,55,190,78,288],
     "n2" : [23,156,199,10]'''

import json

n=10

number ='''
{
 "n1" : [12,55,190,78,288],
 "n2" : [23,156,199,10]
 }
'''
json_numbers = json.loads(number)
print('type of',type(json_numbers))
print('key value')
for key, value in json_numbers.items():
    if int (key [1:])%2==0:
      print(key,':',value)





