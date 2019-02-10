def main():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    c=[]
    for b in a:
        if b%2 == 0:
            c.append(b)

    #one line code
    d = [element for element in a if element%2 == 0]

    print (c)
    print ("One line code result :" , d)

main()

