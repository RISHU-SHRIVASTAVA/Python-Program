num=int(input("Enter Number to check whether it is prime or not :"))
flag=False
if num>1:
    for i in range(2,num):
        if(num%i==0):
            flag=True
        break

else:
    print("Enter Number greater than 1")

if flag:
    print("Given Number is not a Prime Number")
else:
    print("Given Number is Prime Number")

