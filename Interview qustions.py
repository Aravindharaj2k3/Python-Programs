'''
#Given data1 = (12,44,78,90,11,231,50,67,121,,…....and so on)Sum all the two digit odd number. Print the total and the avg
sum_of = 0
count =0
data1 = (9,4,5,12,44,78,90,11,231,50,67,121)
for i in data1:
  if i >=10 <100 and i %2 == 0:
      sum_of +=i
      count +=i
if count >0:
    avg = sum_of/count
else:
    avg=0
print(f'sum of two digit number{sum_of}')
print(f'total two digit count values{avg}')
'''
    
'''

#Use filter and lambda to solve this data1 = {10,73,151,7,55,41,65,117,75,70,19,29,39,100,40,200,44,18}sum all the numbers in the range of 40 to 70 (both the range NOT inclusive)
data1 = {10,73,151,7,55,41,65,117,75,70,19,29,39,100,40,200,44,18}
sum_of_no =0
lst = list(filter(lambda n:  40<= n <70,data1))
print('40 to 70 bwtween values',lst)
sum_value = sum(lst)
print('sum of the values',sum_value)

               
#Using the loop display the following 1213 1415 16 1718 19 20 21

data = [1213,1415,16,1718,19,20,21]
for i in data:
 print('list of elements',i)
'''
'''    
#data1 = [""Surya"",""Avinash"",""Jaya"",""Uday Kumar"",""Anu"",""Palani"",""Vinu""]process the above data1 and find the name which is having maximum length and display its position in the data1
data1 = ["Surya","Avinash","Jaya","Uday Kumar","Anu","Palani","Vinu"]
data =max(data1,key=len)
print(data)


data1 = ["Surya","Avinash","Jaya","Uday Kumar","Anu","Palani","Vinu"]
max_number= data1[0]
for i in data1:
    if len(i) > len(max_number):
        max_number = i
print(f'max string values:{max_number}')
'''
'''
#dict1 = { 100 : 'Arun', 200 : 'Vijay', 345 : 'Kiran'}dict2 = {500:'Vani', 181: 'Ramesh' }create a new dictionary which add all the contents of dict1 and dict2


dict1 = { 100 : 'Arun', 200 : 'Vijay', 345 : 'Kiran'}
dict2 = {500:'Vani', 181: 'Ramesh' }
dict1.update(dict2)
print('add the dictionary elements',dict1)
'''
'''
#use the while loop to display all the numbers in the given start range and end range with a step valueFor example start range is 45 , end range is 123 and step value is 5sum all the displayed number and print the total
#for loop
for i in range(45,123,5):
    print(i)
    
#while loop
i =45
while i <123:
    print(i)
  i+=5
  '''
#given data1 = ""Bangalore 120 Mysore 35 Hassan 117 Managlore 231 Mandya 50 Bijapur 116""process the string and sum all the numbers as available in the string

data1 = ['Bangalore 120', 'Mysore 35', 'Hassan 117', 'Managlore 231', 'Mandya 50', 'Bijapur 116']
sum_data = []

for i in data1:
    split_data=int(i.split()[-1])
    sum_data.append(split_data)
    print('split data',split_data)
tot_sum = sum(sum_data)
print('Total value',tot_sum)
