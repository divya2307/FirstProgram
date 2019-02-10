import random

count = 0

inp = "yes"
while inp.lower() != 'no':
    guess = int(input("Enter the number you want to guess"))
    num = random.randint(1, 9)

    if num == guess:
        print("You guessed it right")
        print(num)
        count += 1

    elif num > guess:
        print("You guessed very low")
        print(num)
        count += 1

    else:
        print("You guessed very high")
        print(num)
        count += 1

    inp = input("Do you wish to continue: Yes/No")
    if inp.lower() == 'no':
        break
    else:
        continue

print("You have guessed %d times" % count)
