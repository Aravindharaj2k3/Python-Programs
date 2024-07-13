'''a1='Bangalore'
a2=454
def aravind():
    print('Location is',a1)
    print('Pincode',a2)
aravind()


def raju():
    loc ='Chennai'
    pin ='632603'
    print('Loction is a:',loc)
    print('Pincode is a:',pin)
raju()

def data_set(data):
    count = 0
    tot_sum =0
    per =0
    count = len(data)
    for i in data:
        tot_sum +=i
    per = tot_sum / count    
    return count,tot_sum,per
data=[10,202,303,293,845,524,54]
a1,b1,c1 = data_set(data)
print("Count of data values is",a1)
print("Sum of values is",b1)
print("Percentage is ",c1)




def aravind(a):
    count=0
    tot_val=0
    avg=0
    sort=[]
   #count= len(a)
    sort=sorted(a)
    for num in a:
        count +=1
        
    for i in a:
        tot_val +=i
    avg = tot_val/count
    return count,tot_val,avg,sort

print("Start the main program")

a =[45,65,3,43,45,3,543,34,334,3,24,3453,45,3]
a1,b2,c3,d4 = aravind(a)
print("Sorting the value is:",d4)
print("Count of values is:",a1)
print("Sum of values is:",b2)
print("Average of values is:",c3)
print("End the main program")
      
'''




def age(value):
        if value >=18:
            print("Your Eligble For Vote Candicate")
        else:
            print("Not Elegibale Candicate")
print('Main fuction is started')
value =int(input("Enter a the age"))
age(value)











