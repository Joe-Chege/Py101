#Creating multiple classes and inheritance

class University:
    def admission(self, school, department):
        print("Welcome to the University of Baraton")
        print("Hi, I am from the", school)
        print("And my department is", department)



class Education:
    def subjects(self, maths, physics, chemistry):
        print("This are the subjects ", maths, physics, chemistry)
        print("I think ", physics, "is the best of all.")

class Student(University,Education):
    def details(self, name, age):
        print("Hi am", name ,"and am", age,)

#Getting objects
person1 = Student()

#what will be displayed

person1.details("Joe-Chege", 26)
person1.admission("Science and Technology", "Technology")
person1.subjects("Engineering maths", "Thermo dynamics", "Engineering Chemistry")



