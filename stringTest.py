var1 = "Guru99!"
var2 = "Software Testing"

print("var[0]:",var1[0])
print("var2[1:5]"+var2[1:5])

if "Soft" in var2:
    print("True")

#print raw string \n

print (r"\n")
print ("\nThis is test")

x = "Divya"
y = "Prabhu"

#string concatination
print (x+y)

#string repetation
print (x*2)

x = "Hello World!"
print(x[:6])
print(x[0:6] + "Guru99")

#use of replace method
oldstring = "I Like Painting"

newstring = oldstring.replace("like","love")

print(oldstring)
print(newstring)

#Upper and Lower

print(oldstring.upper())
print(newstring.lower())
print(oldstring.capitalize())

#join test
print(":".join(oldstring))

print(oldstring)

#reverse
print(" ".join(reversed(oldstring)))

#split
print(oldstring.split("i"))
print(oldstring.split(" "))