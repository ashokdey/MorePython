# Using for loops to iterate
# The basic syntax is : 
# 		for anyVariable in range (startingValue, endingValue + 1, increment ) :
# 				statements

print("Using for loop")

# We can generate number sequence with range() function 
# The range() function returns a stream of numbers with a specified range

for a in range (1, 6) :  
	print (a)

# Using the increment 

print ("Using increment by 2")

for b in range (0, 11, 2) :
	print (b)

# using range only

print ("using range only")

for c in range (5+1) :
	print(c)


# We can print lists, tuples and dictionaries using for loop very easily.

# Creating a list 
shoppingList  = ["bread", "milk", "butter"]
# Printing using for loop as follow 

for item in shoppingList :
	print(item)

print("\n\nIterating multiple lists\n")

# Nice trick to iterate in multiple lists in parallel 
# Creating 4 lists 

days = ["Mon", "Tue", "Wed"]
drink = ["Cofffee", "Tea", "Mango Juice"]
eat = ["Rice", "Chapati", "Dosa"]
workOn = ["Python", "NodeJs", "C++"]

# Iterating in all the above lists in parallel

for day, drink, food, work in zip(days, drink, eat, workOn) :
	print(day, " : drink ", drink, ", eat : ", food, " and work on : ", work)


# More on range() function : 
# --------------------
# List Comprehensions
# --------------------
# We can make a list of integers from 1 - 5 as follow :

myIntList_1 = []

for number in range(1, 6) :
	myIntList_1.append(number) 

print("Printing integer list : ", myIntList_1)

# There is another way to do the same thing 

myIntList_2 = list(range(1,6))
print("Printing integer list : ", myIntList_2)

# The more proper way of doing a list compression is as follow :
# myList = ['expression' for 'item' in 'iterable' ]

myIntList_3 = [number for number in range(1, 6)]
print(myIntList_3)

myIntList_4 = [number - 1 for number in range(1, 6)]
print(myIntList_4)

# using more of the list compression types 

myIntList_odd = [number for number in range(1, 21) if number % 2 == 1 ]
myIntList_even = [number for number in range(1,21) if number % 2 == 0]

print("more on list comprehension")
print("List odd : ", myIntList_odd)
print("List even : ", myIntList_even)


# This comprehensions works for Dictionary as well, but has a ddifferent syntax
# It does not works for tuples