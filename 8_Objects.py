# For creating objects in Python we need to define a class and then we need to
# create the instances of the class which is called as objects

# lets create an empty class 
class FirstClass():
    pass
    
# the above is the most simplest form of class we can create in Python
# let's create the object of the above class 

obj_1 = FirstClass()
print (obj_1)

# An 'obj_1' object has been created
# Adding data members to the classs 

obj_1.name = "myNameIsObject_1"
obj_1.grade = "A"

print(obj_1.name)

# Adding functions/methods inside a class 
# lets create a class of student and add a reset function to reset the value to default

# Functions inside classes are known as methods. Methods are similar to function
# but methods have one required argument called as 'self'. 
# The self argument is just the reference to the object on which the method has been invoked.

class Student() :
    def reset (self) :
        self.name = "Default"
        self.grade = "None"

student_1 = Student()
print(student_1)

student_1.name = "Ashok"
student_1.grade = "A"
print("Name is : " + student_1.name + "\nGrade is : " + student_1.grade)

# calling the reset object on 'student_1' to reset the values 

student_1.reset()
print("After reset :")
print("Name is : " + student_1.name + "\nGrade is : " + student_1.grade)

# using 'hasattr()' to check if the object has an attribute or not

print("Checking 'hasattr'")
print(hasattr(student_1, "age"))  

# If will give output as false, because there is no 'age' preperty in class Student
# Lets add the age property using 'setattr()'

print("Setting age property")
setattr(Student, "age", 20)

# The setattr() takes 3 arguments (classname, property, value)
# Checking for age property

print("Checking again")
print(hasattr(Student, "age"))

# using the getattr() function to get the value of a property given by setattr()

print("Using getattr()")
value = getattr(Student, "age")
print(value) 

# using the delattr() to deleter attributes/properties from a class set by the setattr()

print("Using delattr()")
delattr(Student, "age")

print(hasattr(Student, "age"))    
# The above line will print false as the age attribute has been deleted.


# Now if you remove the 'self' argument from the method declaration and try to call it 
# you'll get an error, lets try it

class NewClass():
   	def withoutSelf():
   		print("it will print error")

myObject_1 = NewClass()
#myObject_1.withoutSelf() 

# Error : TypeError: withoutSelf() takes 0 positional arguments but 1 was given
# The 1 argument that was given by Python is the 'self' argument, so we need to pass 
# an argument 'self' to the method.

# You can write anything instead of 'self'. Those familiar with C++ and Java 
# can use 'this' as well but 'self' is more meaningful

class NewClass():
   	def withoutSelf(this):
   		this.x = 10
   		this.y = 20
   		print("it will NOT print error\nValues are : ", this.x, ", ", this.y)

myObject_2 = NewClass()
myObject_2.withoutSelf() 
