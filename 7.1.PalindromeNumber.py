n=int(input("Enter Number :"))

temp=n
rev=0
while (temp>0):
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10


print("Reverse Number :",rev)

if rev==n:
    print('Number is palindrome')
else:
    print('Not Palindrome')
