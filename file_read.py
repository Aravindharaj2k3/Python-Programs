f=open("D:\\Pyhton practice code\\Writing file.txt","a+")
print('keep entering the text STOP when you type QUIT')
while True:
   data = input()
   if data.upper() == 'QUIT':
      break
   else:
      f.write(data)
      f.write('\n')
print('writing the file is over ')
f.close()
print('\n reading the contents of the file .... \n')
f=open("D:\\Pyhton practice code\\Writing file.txt","r")
data = f.read()
print(data)
f.close()

