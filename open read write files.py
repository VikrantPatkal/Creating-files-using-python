'''f=open('K22PK.txt','w')
f.write('Welcome to file handling\n')
f.write('My name is abc')
f.close()'''

#opening and readiing from files
'''f=open('K22PK.txt','r')
content=f.read()
print(content)'''

'''f=open('K22PK.txt','r')
for content in f:
    print(content,end='')'''


#counting no. of lines
'''f=open('K22PK.txt','r')
count=0
for x in f:
    count=count+1
print(count)'''

#counting no. of spaces:
'''f=open('K22PK.txt','r')
count=0
space=0
char=0
for x in f:
    count=count+1
    space=space+len(x.split())
    char=char+len(x)
print('No. of spaces',space)
print('Number of characters in file is:',char)'''


#import pickle
'''d1={1:'Java',2:'Programming',3:'Python',4:'Language'}
fw=open('pickle1','wb')
pickle.dump(d1,fw)
fw.close()

fr=open('pickle1','rb')
x=pickle.load(fr)
try:
    while True:
        print(x)
        x=pickle.load(fr)
except:
    print('All data read')'''



'''students=[[1,'Rohit',786],[2,'Mohit',876]]
fst=open('studentdata','wb')
for x in students:
    pickle.dump(x,fst)
fst.close()
fst=open('studentdata','rb')
y=pickle.load(fst)
try:
    while True:
        print(y)
        y=pickle.load(fst)
except:
    print('No data left')'''





'''f=open('K22PK.txt','r')
#s=f.read()
#print(s)

s=f.read(6)
print(s)

print(f.read())
f.seek(0)
print(f.read())'''

#write a prog to append the content of one file  at the end of another file.
'''f1=open('K22PK.txt','a')
f2=open('python notes.txt','r')
f1.write(f2.read())
f1.close()
f2.close()
f=open('K22PK.txt','r')
print(f)'''


'''n1=int(input('n1:'))
n2=int(input('n2:'))
print('Going to Divide')
try:
    print('Division is:',n1/n2)
except:
    print('Divison by zero is not possible')
print('Division Done')'''




















































