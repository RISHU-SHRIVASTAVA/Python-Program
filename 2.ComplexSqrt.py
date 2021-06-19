import cmath

num1= eval(input("Enter the Complex Number :"))

num_sqrt= cmath.sqrt(num1)

print(f"Square root of {num1} is :",num_sqrt)
print("Real part :",num_sqrt.real)
print("Imaginary part :",num_sqrt.imag)
