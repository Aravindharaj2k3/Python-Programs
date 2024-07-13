Data1 =[23,45,65,43,22,33,22,55,6,5,44,32,22,45,332]
data2 = list(filter(lambda n: n%2==1,Data1))
print("This is for Odd number of values",data2)
for i in data2:
    print("Odd Numbers",i)
'''
data3=list(filter(lambda n: n%2==0,Data1))
print("This is for Even numbers",Data1)
for j in data3:
    print("This is for Even numbers",j)


    
Data1 =[23,45,65,43,22,33,22,55,6,5,44,32,22,45,332]
data4 = list(filter(lambda n: n >=10 and n<=65 and n%2==0,Data1))
print(data4)


'''
