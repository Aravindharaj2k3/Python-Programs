# given data1 = [12,660,101,18,902,299,4,117,2,5,29,156,19,126,39]
#write a function to check how many numbers are above 500
#find the sum of those numbers
#find the avg of those numbers

'''data1 = [12,660,101,18,902,299,4,117,2,5,29,156,19,126,39]
data2 = max(data1)
data3 = min(data1)
print('Max number in data:',data2)
print('min number in data:',data3)'''



data2 = ['Uday','Alexander','Umesh','Jayanth','Ajay','Kiran','Amit','Ganesh','Akash']
def aravind(data):
    count = 0
    for name in data:
        if name.startswith('A'):
            count += 1
    return count
count = aravind(data2)
print("Number of names starting with 'A':",count)
