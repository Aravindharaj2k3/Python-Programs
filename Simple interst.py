'''si= lambda p,t,r :(p*r*t)/100
amt = lambda interst,p:interst+p
principle =10000
rate=7.5
time=3
interst = si(principle,rate,time)
print(interst)


si=lambda p,t,r :(p*t*r)/100
amt=lambda interst,p:interst+p
principle =10000
rate=5.6
time=5
interst=si(principle,rate,time)
print(interst)


#===============================================
3) given data1 = [12,66,11,18,90,299,4,17,2,5,29,155,19,6,39]
   pass this to a function
   the function should return sum of all the TWO digit number
   the function should return avg of all the TWO digit number
   the function should return highest & lowest TWO digit number


def process_data(data1):
    count =0
    c=0
    for i in data1:
        if 10>= i<=99:
            count+=1
    for num in data1:
        if num>=10 and num<=99:
            c=c+i
        f=c/count
        return c,count,f
print("Start the main block")

data1 = [12,66,11,18,90,299,4,17,2,5,29,155,19,6,39]
a1,b1,c1 = process_data(data1)
print("Sum of the values",a1)
print("Count of the values is",b1)
print("Average values is",c1)

print("End the main block")
'''
data1 = [12,66,11,18,90,299,4,17,2,5,29,155,19,6,39]
data2=list(filter(lambda n: n%2==1,data1))
print(data2)
for i in data2:
    print("Odd Numbers",i)
data3=list(filter(lambda n: n%2==0,data1))
print("Number of even",data3)
for j in data3:
    print("Even Numbers of",j)

    



