import time
import math

def is_prime(num):
    if num<=1:
        return False

    max=math.floor(math.sqrt(num))

    for i in range(2,max+1):
        if(num%i==0):
            return False
    else:
        print(num,end=' ')
    return True

t=time.time()
c=0

num=int(input("Enter Number :"))
print("Prime Number List :")
for n in range(num+1):
    x=is_prime(n)
    c+=x
print()
print("Total Prime Number :",c)

t1=time.time()
print("Time Required :",t1-t)

