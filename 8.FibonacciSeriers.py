x,y=0,1
temp=0
n=int(input("Enter length of Fibonacci series :"))

if n==1:
    print(x,end=' ')

elif n==2:
    print(x, y, end=' ')

elif n>2:
    print(x, y,end=' ')
    while(n>2):
         temp=x+y
         print(temp,end=' ')
         x,y=y,temp
         n-=1

else:
    print("Please enter number greater than 1 ")
