# python program - prime number

num = int(input("enter a number to check prime: "))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(num, "is not prime")
            break
    else:
        print(num, "is prime")
else:
    print(num, "is not prime")
