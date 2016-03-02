# Lists are collection of different data types
# Lists maintains an order
# Lists are mutable 
# List can contain repeated items/elements 

# Can be created in 2 ways 
# First way - []
# Second way - list() function : this converts other data types into list


myList_1 = [] # An empty List
print ("\nPrinting an empty List :", myList_1, "\n")

myList_2 = ["Any", 2, 3.4, 'c', "green"]
print("Simple list : ", myList_2, "\n")

myList_3 = ["Python", 3, 3.4, "Java", 3, 'c', 'c'] # List can contain repeated values
print("List with repeated values :", myList_3, "\n")

# Creating lists with 'list() function' 
print("\nCreating lists with 'list() function'\n")

myString = "I am learning Python"
myList_4 = list(myString)
print(myList_4, "\n")

