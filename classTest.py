class myClass():
    def method1(self):
        print("I am the first method of this class")

    def method2(self,var):
        print("I am the Second Method of tis class. Hello "+ var)

class childClass(myClass):
    def method1(self):
        print("I am te child class method")

def main():
    c = myClass()
    c2 = childClass()
    c.method1()
    c.method2("Divya")
    c2.method1()
    #c2.method1()

if __name__ == "__main__":
    main()