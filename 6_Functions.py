# Functions are used for code reusablity
# We use the keyword 'def' to define a function followed by the nem of the function
# Even if the function o not have any parameters, the '()' and ':' is required

# sample function 
def hello () :
	print ("Hello user")

# calling the function 
hello()

# now lets take name from the user 
# creating function wth parameters

def helloUser (name) :
	print("hello ", name)

# calling the function with argument 'John'
helloUser("John")

# Lets make it more interactive, take the name from user and greet them

#userName = input ("Please enter your name :")
#helloUser(userName)

# Function that return a value 

def sum(num1, num2):
	return (num1 + num2)

sumofnos = sum(5, 9)
print(sumofnos)

# directly calling the function iside another function
print(sum(23, 56))

# Function returning a boolean value 
def isAgree () :
	return True

if (isAgree()) :
	print("Rerurned true")
else :
	print("returned false")

# Function returning None

def returnNone () :
	pass

# 'pass' keyword is used when we do not want to do anything, 
# means we say to python :just pass, do whatever you want 
# 'pass' can be used inside if-else block,  for-loops, while-loops and functions as well

# calling the returnNone()

print("Function with return pass returns : ",returnNone())

myVar = returnNone()

if myVar is None :
	print("Returned none")
else :
	pass

print("pass in work inside else block")

# function with variable number of arguments or varagrs
# it takes the arguments as a tuple
print("\nVariable length arguments :\n")
def varArguments (*args) :
	print("here is the tuple returned by args in *args : ", args)
	return None


# Calling varargs function 

varArguments("Ashok", "Java", 1, 4.5643)

print()

# We can also take the key-value pairs as an arguments :
# it takes the arguments as a dictionary 

def varArguments_2 (**args) :
	print("here is the dictionary returned by args in **args :", args)
	return None

# calling the above function with key value pair 
varArguments_2 (food='bread', day='monday', desert='sweet')

print()
print("Docstring here :\n")


# --------------------------
# DOCSTRING
# --------------------------

# Adding documentation to the function 
# we can addd documentation to our functions so that when the users tries to 
# call help() on our function, we can show it's documentation to the developer
# Wee can attach our documentation at the beginning of the function
# calling help() on the previous functions we created

help(sum)
# Or we can call the 'docstring' that is attached to our function
print ("printing the help document")
print(sum.__doc__)

# the above call to the '__doc__' will return 'None'
# lets add some documentation to our function

def greetUser (name) :
	'This function greets the user with his/her name and returns none'
	print("Hello ", name)
	return None

# Calling help on the above function

print("\nprinting help() on greeUser()")
print()
help(greetUser)

print("printing help doc of greetUser()")
print(greetUser.__doc__)

