class Employee():
    # pass
    increment = 1.5
    count_instance = 0
    def __init__(self,fname,lname,post,salary):
        self.fname = fname
        self.lname= lname
        self.post = post
        self.salary = salary
    def increase(self):
        self.salary = self.salary  * Employee.increment

    # @classmethod
    # def count_instance(cls):
    #     return f"you have created {cls.count_instance} instance of Employee class"

    @classmethod
    def from_str(cls, emp_string):
        fname,lname,post,salary = emp_string.split("-")
        return cls(fname,lname,post,salary)


# emp1 and emp2 is an argument
emp1 = Employee("vikas","jaiswal","developer", 22000)
emp2= Employee("aditya","gautam", "manager", 20000)
class Programmer(Employee):
    # pass
    def __init__(self, fname,lname,post,salary,proglang,exp):
        super().__init__(fname,lname,post,salary)
        self.proglang = proglang
        self.exp = exp



emp4 = Programmer("vikas","jaiswal","programmer",50000,"python","1year")

print(emp1.salary)
# emp1.increase()
print(emp1.salary)

emp3 = Employee.from_str("ambuj-tripathi-HR-25000")
print(emp3.fname)

print(emp3.salary)

print(emp4.post)
# print(Employee.count_instance())