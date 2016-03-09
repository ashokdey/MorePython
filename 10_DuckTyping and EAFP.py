# Duck Typing
# ==========
# It is a term used in dynamic languages that do not have strong typing.
# The idea is that you don't need a type in order to invoke an existing method on an object - 
# if a method is defined on it, you can invoke it.
# 
# The name comes from the phrase "If it looks like a duck and quacks like a duck, it's a duck"
# 
# The above para is extracted from stackoverflow.com
# Lets seee the above in codde 

class Duck:
	def quack(self):
		print("I can quack: quck ! ")
	def fly (self):
		print("I can fly : flap flap !")

class Person:
	def quack(self):
		print("I can also quack")
	def fly(self):
		print("I can try to fly !")

class Frog:
	def no_quack(self):
		print("Frogs cannot quck")


# lets create the objects 

duck_one 	= Duck()
person_one 	= Person()
frog_one	= Frog()

# Create a function to whic we'll pass the object of each class and invoke the method quck() and fly()

def quck_fly (obj):
	try :
		obj.quack()
		obj.fly()

	except (AttributeError) :
		print("Cannot invoke 'quack()' and 'fly()' on :", obj)


# Lets pass the all the three objects to the above function

quck_fly(duck_one)
quck_fly(person_one)

# quck_fly(frog_one)		# we'll get an error coz the Frog class don't have any quack() or fly() method


# EAFP : Easy to Ask forgiveness than Permission
# ==============================================

# Duck Typing and EAFP goes hand in hand most of the time. 
# EAFP basically says that try to do instead of checking. 
# Lets make it more clear with the following example 

# lets create a list and try to print an element from it without getting an index error 
# an we'll do that in a non pythonic way 

my_list = [1, 2, 3, 4, 5]

if len(my_list) >= 5 :
	print(my_list[4])
else :
	print("Index error")


# In the above code we're actually checking for the index before printing the element
# Lets do it in pythonic way, the EAFP way !


try :
	print(my_list[4])
except IndexError :
	print("index error !")


# The above is more efficient and more readable. 
# let's take another example 

# The other no pythonic example will be of the 'quack_fly()' method

def quack_fly_2(obj):
	if isinstance(obj, Duck) or isinstance(obj, Person):
		obj.quack()
		obj.fly()
	else :
		print("Not an object of quack family")

print("\nInvoking 'quack_fly_2()'")

# Invoke the above method

quack_fly_2(duck_one)
quack_fly_2(person_one)
quack_fly_2(frog_one)