# Most Object Oriented languages have the concept of a constructor 
# that initializes the object when it is created.
# Those famaliar with Java and C++ uses the following syntak to create and initialize an 
# Object : 
# Object myObject = new Object()
# where the 'new' operator creates an object named 'myObject' and the 'Object()' initializes the object 
# with default values. Python has both constructor and initializer. lets start with the initializer. 

# lets create a point class that requires us to supply 'x' and 'y' coordinates when the 
# point object is instantiated


class Point():
	'Class to represent the 2D plane points x and y'

	def __init__ (self, x=0, y=0):
		"Initiallize the position of the points with the user given points, if the user doesn't give any value, then it starts from the origin"
		self.move(x, y)

	def move(self, x, y):
		'''Move the points to a new location'''
		self.x = x;
		self.y = y;

	def reset (self, x, y):
		"""Resets the point back to origin"""
		self.move(0, 0)

	def display(self):
		"Desplays the values of the points"
		print ("The points are x : ", self.x, ", y: ", self.y)


# Docstring has been used here.
# Creating objects

point_1 = Point(10, 20)
point_1.display()

# using the help function to get the docstring of the class

#help(Point)

print("Inheritance here : ")

# ==========================
# INHERITANCE
# ==========================

# Inheritance simply means creating a new class from the existing class with some changes 
# it is an exccellent way to reuse code.

class Car():
	def describeYourself(self):
		print("I am a car")

class Ford(Car):
	pass


# Creating objects 

varCar = Car()
varFord = Ford()

varCar.describeYourself()
varFord.describeYourself()

# Both will execute and will print the same output
# This proves that the class 'Ford' inherited the method 'describeYourself()' from Car class


# Method overriding
# =================

# We need to change the method in the parent class to make it more appropriate for the classFord
# This process of changing the parent class method is called as method overrriding

print("method overriding...")

class Mustang(Car):
	def describeYourself(self):
		print("I am Mustang")


varCar.describeYourself()
# Will print "I am a car"

varMustang = Mustang().describeYourself()
# Will print "I am mustang"


# We can override each method that comes from the parent class and can also add extra methods
# in the child class 
# lets create a class Animal and its child classes

class Human():
	def __init__(self, name):
		print("my name is : ", name)

class Indian (Human):
	def __init__(self, name):
		print("I am Indian, my name is : ", name)

	def namaste(self):
		print("Namaste to all")


varHuman = Human("AnyName")
varIndian = Indian("Ashok")
varIndian.namaste()

print("Using 'super()'\n")

# Using the super() function to call the parent class methods
# Lets a class mamals that has an initializer and initializes the name attribute
# Then we will create a child class Human inheriting mamals 
# We will call the init method of parent class ffrom the child class using super()


class Mamals () :
	def __init__(self, name):
		self.name = name
		
class Human(Mamals):
	def __init__(self, name, country):
		super().__init__(name)
		self.country = country

	def introduce(self):
		print("My name is : ", self.name, "\nI am from : ", self.country)


varHuman_2 = Human("Ashok", "India")
varHuman_2.introduce()


# When we define the __init__() method in our child class the parent class __init__() method is replaced
# and is not called automatically anymore. Hence we use super() to call it explicitly.

# In Python there is no access specifiers like private, protected and public. 
# In python everything is public and can be accessed from anywhere
# There is a Name Mangling technique that Python use to hide data members (Not so strictly)
# you can name a data member followed by 2 underscores to hint python that you're trying to make it private

print("\nName Mangling\n")

class NameManglingDemo():
	def __init__(self, name):
		self.__name = name

	@property
	def name(self):
		print("Inside Getter")
		return self.__name

	@name.setter
	def name(self, name):
		print("Inside setter")
		self.__name = name

# Decoraters ('@property' and '@name.setter') has been used in the above class
# Now lets create an object of the above class

manglingDemo = NameManglingDemo("Ashok")

# getting the name 

print(manglingDemo.name)

#Settting the name 
manglingDemo.name = "New Ashok"

# But we cannot directly access __name
# Lets try 

# print(manglingDemo.__name)		# This line will give an error 

# however it is also not fully secure or private to the class
# we can still access it like below :
print("Directly accessing '__name':")
print(manglingDemo._NameManglingDemo__name)

# Name Mangling is not a perfect protection, it just discourages from accidental or 
# intensional direct access to the attribute.