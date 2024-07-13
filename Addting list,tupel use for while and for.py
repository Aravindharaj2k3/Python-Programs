print("Stop for the value is 5")
value =[]
while True:
    Data = input("Enter the values of number & values")
    if Data == '5':
        break
    value.append(Data)
    for i in value:
        print('Print the values for items',i)
