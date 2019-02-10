import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


c = [x for x in set(a) if x in b]

print(c)

# randomly generate number list

list1 = random.sample(range(1,30),12)
list2 = random.sample(range(1,30),16)

