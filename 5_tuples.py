# Tuples are similar to lists but they are immutable, i.e. once created we cannot add, 
# delete or modify and item in the tuple.

# Creating empty tuple 

myTuple_1 = ()
print (myTuple_1)

myTuple_2 = ("India", "USA", "Japan", "China")
print(myTuple_2)

# Printing using a loop

for item in myTuple_2 :
	print(item, end=" ")
print()

# By default, the print function adds a '\n' after each output
# we can modify it by using [end = ' ' ] after the argument to the print function

# We can also create a tuple without using the '(' and ')'

myTuple_3 = "India", "USA", "China", "Japan"
print(myTuple_3)

# Converting a list into a tuple using the 'tuple()' function
# The 'tuple()' function can be used to convert different data types to tuples

myList_1 	= ["Bread", "Milk", "Butter", "Tea"]
myTuple_4 	= tuple(myList_1)
print(myTuple_4)


# Tuples can be used to assign multiple variables at once 
# Also known as Tuple Unpacking
# 				---------------

a, b, c, d = myTuple_4
print("a = ", a)
print("b = ", b)
print("c = ", c)
print("d = ", d)

# We can use tuples to exchange values in one stateemnt without using temporary variable

num_1	= 10
num_2	= 20

num_1, num_2 = num_2, num_1

print( "Num 1 = ", num_1, "\nNum 2 = ", num_2)

# Few points regarding Lists vs. Tuple 

# 	Tuples use less space 
# 	We can't clobber/change tuple items by mistake
# 	We can use tuples as dictionary keys 
# 	Named tuples can be an alternative to objects
# 	Function arguments are passed as tuples 
