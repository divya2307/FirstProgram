Dict = {
    "Div":29,
    "Sun":34,
    "Sam":25
}

print(Dict["Sun"])

#Dictonary copy
Boys = {
    "Sun":34,
    "Adi":45,
    "Nit":27
}

Girls = {
    "Div":29,
    "Sam":25
}

StudentsBoys = Boys.copy()
StudentsGirls = Girls.copy()

print(StudentsBoys)
print(StudentsGirls)

#Updating dictionary

Dict.update({"Sar":23})
print(Dict)

#deleting from dict

del Dict ["Sam"]
print (Dict)

#Dictionary Item method
print("Students name: %s" %list(Dict.items()))

#Dictionary Key
for key in Dict.keys():
    if key in Boys.keys():
        print(key + " Found in Boys Dict")
    else:
        print(key+" Found in Girls Dict")
#Sorting
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
Students = list(Dict.keys())
Students.sort()
for S in Students:
      print(":".join((S,str(Dict[S]))))
