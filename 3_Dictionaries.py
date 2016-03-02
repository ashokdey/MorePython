# Dictionaries in python are similar to a list but the order of items doesn't matter
# And they are not selected by an offset such as 0, 1... so on.
# They are similar to the concept of associative arrays i.e they are key-value pair 
# The key is often a string but they can be any of the immutable type : tulpes, int, flot, string
# If you are familiar with the Javascript Object Literal syntax, then dictionary is quite similar to it


# creating an empty dictionary 
myDict_1 = {}
print(myDict_1)

# Creating a dictionary with key-value pairs

myDict_2 = {
	"Python" 	: 	"A dynamic general purpose language you'll love",
	"day"		:	"A period of 24 hours, generally misspent",
	"month"		:	"A period of 30 days on an avg, few have 31 and feb has 28/29"
}

print (myDict_2)

# Adding ney key-value in dictionary
myDict_2["HTML"] = "Hyper Text Markup Language"

print(myDict_2)

# Printing using a loop 

print("\nPrinting a dictionary using for-loop\n")
for keys in myDict_2 :
	print(keys," : ", myDict_2[keys])


# Copying a dictionary 

myDict_3 = myDict_2.copy()
print(myDict_3)

# Delete a single key-value pair

del myDict_3["HTML"]
print(myDict_3)

# deleting all the items in a dictionary using 'clear()'
myDict_3.clear()
print(myDict_3)


print("Printing myDict_2")
print(myDict_2)

# Printing all the keys in a dictionary
print("\nPrinting the keys of a dictionary\n")
print (myDict_2.keys())


# Storing keys in a custom list 
keysList = list (myDict_2.keys())
print("\nPrinting the keys of dict in a list :: ", keysList)


# storing all the values in a custom list 

valueList = list(myDict_2.values())
print("\nPrinting the values of dict in a list :: ", valueList)


# Storing both items and values in a list 
# The key-values are returned as a list 

keyValueList = list (myDict_2.items())
print ("\n\nKey values in a list :: ", keyValueList)

# The zip() function
# The zip function is used to combine tuples, the value returned by the zip() function is not a 
# tuple or a list instead it is an iteratable value that can be turned into a list or tuple or a dictionary
# lets try it

# Weekdays in english and french (creating tuples)
print("\n\n")
engWeek = "Monday", "Tuesday", "Wednesday"
frenceWeek = "Lundi", "Mardi", "Mercredi"

myWeekList = list (zip(engWeek, frenceWeek))
print(myWeekList)

myWeekDict = dict (zip(engWeek, frenceWeek))
print(myWeekDict)