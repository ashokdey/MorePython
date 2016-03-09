# ================================
# Function as First Class Objects
# ================================

# In python, everything is a object. The numbers, strings, lists, 
# tuples, dictionaries and functtions as well.

# Function are first class objects, we can assign them to variables
# use them as an argument to other functions and can return them from functions.

# Lets define a function 

def simpleFunction () :
	print ("hello")

# Calling the function 
simpleFunction()

# The above will give an output as : hello

# Lets make a function with a function as it's parameter
def someFunction (func) :
	print ("Calling the function given as an argument")
	func()

# In the abpve example, the 'someFunction' has an argument 'func' : name of the function
# and inside the body of the function, it will call the function given as an argument
# lets try calling it 

someFunction(simpleFunction)

# lets try out one more 

def sumOfNumbers (num1, num2 ) :
	print(num1 + num2)

def doAddition (func, num1, num2) :
	func(num1, num2)

# lets call the function 'doAddition' 
doAddition (sumOfNumbers, 20, 35)

# ========================================
# INNER FUNCTIONS
# ========================================

# We can define a function withing another function 

def outerFunction(a, b) :
	def innerFunction (c, d) :		
		return a + b 				
	return innerFunction(a, b)		 
									
# innerFunction with 2 parameters and  returning the sum of two numbers							
# the outer function is returning the value returned by the inner function 
# and the inner function is passed the argumets of outer function

# Lets call the above function
print("\n Inner Functions.........\n")
outerFunction(10, 33)


# ==================================================
# CLOSURES
# ==================================================
print("\nWelcome to CLOSURES\n")

# An inner function can act like a closure. A Closure is a function that is dynamically generated
# by other function and can both change and remember the values of the variables that were created
# outside the function

# A CLOSURE is a function object that remembers values in enclosing scopes regardless of whether those 
# scopes are still present in memory. If you have ever written a function that returned another function, 
# you probably may have used closures even without knowing about them.

def greetUser (message) :
	'this is outer function'
	def greet () :
		'This is inner function'
		print(message)
	greet()

# lets call the function 'greetUser'
greetUser("Hello Folks")

# So we can see that the inner function greet is able to access the variable of the outer function.
# If we try to return the inner function 'greet()' without calling it, what will be the result?

def greetUser_2 (message) :
	def greet_2 () :
		print(message)
	return greet_2

greetUser_2("Hello Programmers ! ")

# Nothing will happen as we are not calling the 'greet_2()'' anywhere, we are simply returning it but
# we are not catching the return value from the outer function 'greetUser_2()'
# Now assigning the return value to a variable 

catchReturn = greetUser_2("Hello Programmers! ")

# Now catchReturn has the function 'greet_2()' inside it. 
# 
print("catchReturn is called")
catchReturn() 

# even if we delete the function greetUser_2(), the data of the function got 
# attached to the variable catchreturn

del greetUser_2
# if we try to call greetuser_2(), it will be an error : greetUser_2 is not defined 
# try calling it 
# greetUser_2("hello Dear")			# romove the comment and execute this line to see the error


# But if we call 'catchReturn()', there will be no error and it will run perfectly, 
# this is called as a Closure 

catchReturn()

# When To Use Closures? What are closures good for? 
# Closures can avoid the use of global values and provides some form of data hiding. 
# It can also provide an object oriented solution to the problem. When there are few 
# methods (one method in most cases) to be implemented in a class, closures can provide 
# an alternate and more elegant solutions. But when the number of attributes and methods 
# get larger, better implement a class.

# =================================================
# LAMBDA Expression/Function : Anonymous Functions
# =================================================

print ("\nWelcome to LAMBDAS")

# Syntax of Lambda = lambda arguments : expressions
# They are ment for very small functions that can be written in a line 
# They act mostly similar to the inline functions in C++ 

# Normal sum function :
def squareNum (num) :
	return num * num

# Lambda for the same : 

square = lambda x : x * x 

# Calling a normal function and a lambda 

number = squareNum (5)
print("Using normal function : ", number)


numberLambda = square(5)
print ("Using Lambda : ", numberLambda)

# here 'square' is a varible that holds th function. 
# if we assign square a value like below : 

square = 10

# then we cannot call that function again
# square(10) # Error here and the lambda function is lost 
