num1 = int(input("Enter a dividend:"))

if num1%2 == 0:
    print(str(num1)+" is an even number")
else:
    print(str(num1) + " is an odd number")

if num1%4 == 0:
    print(str(num1) + " is a multiple of 4")

num2 = int(input("Enter a divisor"))

if num1%num2 == 0:
    print(str(num2)+" divides "+str(num1)+" evenly")
