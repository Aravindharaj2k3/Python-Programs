n= str(int(input("Enter a number")))
digit_sum=0
for i in n:
    digit_sum = digit_sum+int(i)**len(n)
if int(n)== digit_sum:
    print(n, "is an armstrong number")
else:
    print(n, "is not an armstrong number")
