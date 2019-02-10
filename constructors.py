class Employee():
    emp_count=0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.emp_count +=1

    def empcount(self):
        print("Total employees :%d" %Employee.emp_count)

    def displayEmpDetails(self):
        print("Name : ",self.name+" Salary :",self.salary)

def main():
    emp1 = Employee("Divya", 20000)
    emp2 = Employee("Sunny", 60000)

    emp1.displayEmpDetails();
    emp2.displayEmpDetails();

    emp1.empcount()

main()
