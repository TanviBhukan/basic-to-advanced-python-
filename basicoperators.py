# python arithmetic operators

# take input from user
a = float(input("enter first number: "))
b = float(input("enter second number: "))

# addition
print("addition:", a + b)

# subtraction
print("subtraction:", a - b)

# multiplication
print("multiplication:", a * b)

# division
if b != 0:
    print("division:", a / b)
    print("floor division:", a // b)
    print("modulus:", a % b)
else:
    print("division, floor division, modulus: cannot divide by zero")

# exponentiation
print("exponentiation:", a ** b)
