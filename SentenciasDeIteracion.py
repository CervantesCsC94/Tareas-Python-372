SentenciasDeIteracion.py


#----while
i=1
while i<10:
    print(i)
    i+=1 #i=i+1

#-----for
k=1
for k in range(10):
    print(k)

for j,k in enumerate (range(10)):
    print(j)
    print ("k",k)

for item in "[1,2,3,4,5,6,7]":
    print(item*2)

for l, line in enumerate(open("ArchivoDeTexto.txt")):
    print(l,": ",line)
    for p in line.split():
        print(p) 

lista=[]
for i in range (10):
    lista.append(i)
print(lista)

print([i for i in range(10) if i %2==0])


import random
r=1
while r!=99:
    r=random.randint(1,100)
    print(r)

import random
r=1
c=0
while r==99 or c<50:
    r=random.randint(1,1000)
    c+=1
    print(r)