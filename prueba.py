from random import randint


LST=[]

for i in range(10):
    LST.append(randint(-20,20))

print(LST)

c=0

for val in LST:
     if(val>0):
         c=c+1
         
print("El nro de valores positivos es:",c)
