 #List Functions  

#append
my_list=[1,3,5,7,8]
my_list.append(4)
print(my_list)

#Remove
list1 = [1, 2, 3, 'Aravind', 4, 5]
list1.remove(2)
print('List after removal:', list1)

#extend
list1=[1,3,4,5]
list2=[4,5,6,7]
list1.extend(list2)
print(list1)

#insert remove 
my_list.insert(4,9)
print(my_list)
my_list.remove(9)
print(my_list)
my_list.count(2)
print(my_list)

#Reverse
a=[1,2,3,4,5,6,7,8]
list.reverse(1,2,3,4,5,6,7,8)
print(list)

#Tuples functions 
#max
max_value =[54,66,58,22,44,56,58,33,68,45]
mx = max(max_value)
print('Print the max value:',mx)

#min

max_value =[54,66,58,22,44,56,58,33,68,45]
mx = min(max_value)
print('Print the min value:',mx)

#len

str1 ='Aravidharaj'
count_str = len(str1)
print('Total count of string',count_str)

#Sorting
data =[51,55,85,44,55,1,2,4,2,7,5,4,]
data.sort()
print('sorting the list of numbers',data)

#sum
data =[51,55,85,44,55,1,2,4,2,7,5,4,]
sum_value = sum(data)
print('Sum of value',sum_value)

#List of set functions 
#union

data1 ={512,84587,5544,7844,144,1144,44411,5545}
data2 ={154,55,11,22,44554,5544,144,512}
uni_set = data1.union(data2)
print('List of union values',uni_set)

#Intersection

data1 ={512,84587,5544,7844,144,1144,44411,5545}
data2 ={154,55,11,22,44554,5544,144,512}
uni_set = data1.intersection(data2)
print('List of common values',uni_set)

#add
data ={1,2,3,4}
data.add(6)
print('Add the values',data)


#remove
data ={1,2,3,4}
data.remove(3)
print('Remove the values',data)





