f = 101
d = 80
print(f)

def function():
    global f
    print (f)
    f = "this is local defination for f"
    print (f)

function()
print(d)
print(f)
del d # to delete the variable
print(d)