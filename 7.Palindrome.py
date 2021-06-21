n= input("Enter String :")
x=""
for i in n:
     x=i+x

print("Reverse String :",x)

if(x==n):
    print("Given String is palindrome")
else:
    print("Given string is not palindrome ")


