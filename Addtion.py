'''def aravind():
  a = int(input("Enter a number A:"))
  b = int(input("Enter a number B:"))
  Add = a+b
  print("Addtion of two numbers",Add)
aravind()
'''
#age wise vote
'''
num1 = int(input("Enter a Age:"))
if num1 >18:
    print('Vote ellible candicate')
else:
    print("Vote Not eligibe candicate")


strr ='sravindj'
for i in strr:
    print(i)

#Slicing

city = "New Delhi"
if "D" in city:
    p=city.index("D")
    print(p)
    print(city[p])
    p=city.index("D",p+1)
'''
city = "NewDelhi"
if "D" in city:
    p = city.index("D")
    print(p)
    print(city[p])
    p = city.index("e", p + 1)  # corrected "E" to "e"
    print(p)
