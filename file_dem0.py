f = open("D:\\Pyhton practice code\\news.txt","r")
result = f.read(100)
print(result)
lst=result.split()
print('Number of words',len(lst))
sort_lst = sorted(lst)
for i in sort_lst:
     if i == 'Aravind':
        print(i,'Orginal name:')
     elif i == 'Raju':
        print(i,'Pet name:') 
        print(i)
f.close()