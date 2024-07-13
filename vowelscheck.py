ara=['a','A','e','E','i','I','o','O']
names=input('Enter your number')
names2=list(names)
count=0
for i in names2:
    if i in ara:
     count=count+1
if count>=1:
    print('contains vowels')
else:
    print('contains no vowels')
