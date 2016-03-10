# In Inheritance, a class is inherited (extended) by a new sub-class that will add custom attributes 
# and behavior to the inherited ones.

# In Composition, a class is utilized by creating an instance of it, and including that instance inside 
# another larger object.

# To make it simpler and easier to remember, let’s say it in one sentence:
# Inheritance extends (inherits) a class, while Composition uses an instance of the class.

# Let's create a Duck class, Wings class and a Tail class, we all know that a Duck 'has-a' Tail and Wings.

class Wings:
	def __init__(self, length):
		self.length = length

class Tail:
	def __init__(self, length):
		self.length = length

class Duck:
	def __init__(self, wings, tail):
		self.wings = wings
		self.tail = tail

	def about(self):
		print ("I am a duck and I have a ", wings.length, " wings and a ", tail.length, " tail")


# let's create the objects 

wings = Wings('small')
tail = Tail('long')
duck = Duck(wings, tail)

duck.about()