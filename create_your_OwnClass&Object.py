# OOP

# we create our own class and object
# object is a instance of class


class Person():
    def __init__(self , person_name, person_age,person_height):
        self.name = person_name
        self.age = person_age
        self.height = person_height

    def welcome(self):
        print("welcome{}".format(self.person_name))
person1 = Person("vikas", 22 ,"172cm" )
person1.welcome()
print(person1.age)



