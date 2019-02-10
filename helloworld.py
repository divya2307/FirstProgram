print("Hello World")
print("My first Python code")
a = 8
b = 9
print(a + b)


'Hello' == "hello" == """Hello"""

print('hello'.capitalize())

name = "Div"
machine = "Pal"

print("Nice to meet you {0}. I am {1}".format(name, machine))

print(f"Nice to meet you {name}. I am {machine}")

number = 5

if number:
    print("Number is defined and truth")

if number == 5:
    print("Number is defined as 5")

else:
    print("Number is other than 5")


pcourse =True

if pcourse:
    print("This will execute, this is Boolean check, variable defined is TRUE")

if number !=5:
    print("This will NOT execute")

if number ==5 and pcourse:
    print("This is true, AND test. Both conditions mentioned are true")

a = 1
b = 2

print("bigger") if a > b else print("smaller")

students = ["div" , "sun" , "pai" , "prabhu"]

print(students[0])
print(students[1])

print(students[-1])

students[0]="Sai"

print(students[0:])

students.append("Divya")

print(len(students))

print(students.reverse())
print(students[0:])


for name in students:
    print("Student name is {0}".format(name))

