num=int(input("Enter number to check whether it is Armstrong number or not :"))
temp=num
order=len(str(num))
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp=temp//10

if num==sum:
    print("Given Number is Armstrong Number ")
else:
    print("Not a Armstrong Number ")