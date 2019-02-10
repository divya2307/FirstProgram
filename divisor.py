num = int(input("Enter the dividend"))

new_list = list(range(1,num+1))

divisor = []

for number in new_list:
    if num % number == 0:
        divisor.append(number)

print(divisor)