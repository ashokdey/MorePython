# There are several different function/methods that can be used with Lists

# getting an Item/ element in the list using offset
myList = ["India", "USA", "Japan", "Russia", "Australia", "John", "Bob", "Eclipse", "NetBeans"]

#Printing the list 
print(myList)

# Using offset to rethrive India
print (myList[0])

# Using offset to rethrive Russia
print(myList[3])

# Modifying using offset 

print("Value at 'myList[2] before changing :", myList[2])
myList[2] = "Canada"
print("Value at 'myList[2] after changing :", myList[2])


# Extracting sub-list from a list using offset

print(myList[0:4]) 			#Extracted items from index 0 to 3
print(myList[4:7]) 			#Extracted items from index 4 to 6
print(myList[0:8:2]) 		#Extracted items from index 0 to 7 with a gap of 2 items

print(myList[::-2]) 		#Extracted items from the end with gap of 2 items

#Trick to reverse a list 
print(myList[::-1])

# Getting the length of a List 

lengthOfList = len(myList)
print("Length of the list is : ", lengthOfList)

print()

#Add an item at the last using 'append()'
myList.append("VisualStudio")
print(myList)

# Adding an item using offset
myList.insert (2, "China") 
print(myList)
print("Length of the list is : ", len(myList))

# Combining/ merging lists using 'extend()'

myList_2 = ["Java", "Python"]
myList.extend(myList_2)
print(myList)

# Merging again using '+='

myList_3 = ["PHP", "JS"]
myList_2 += myList_3
print("myList_2 : ", myList_2)


# Deleting an item using 'del' 
del myList[3]
print(myList)
print("Length of the list is : ", len(myList))

# Deleting item using 'remove()'
myList.remove('China')	
print(myList)
print("Length of the list is : ", len(myList))

# Deleting with 'pop()'

print(myList.pop(0)) 		# Will return the first element and removes it from the list
print(myList)

print(myList.pop()) 		# Will return the last element and removes it from the list
print(myList)

print(myList.pop(4))  		# Will return the 4th element and removes it from the list
print(myList)

print(myList.pop(-1))		# Will return the last element and removes it from the list
print(myList)

myList.append("USA")
myList.append("India")
myList.append("PHP")
print(myList)

# Count the occurence of an item in a list 
print ("Count the occurence of 'USA' ", myList.count ("USA"))


# Copying a list
myNewList = myList

# Sorting a list using 'sort()' and 'sorted()'
# sort() 		: sort the list in place
# sorted(list) 	: return a sorted list 

myList.sort()
print(myList)

myNewList_2 = sorted(myNewList)
print(myNewList_2)

# Converting a List to a string 
# We need a separator to sepatare the list items in a string 

separator = "-"
myString = separator.join(myList)
print("\n" + myString + "\n")


# Creating copy of a list 

List_1 = myList.copy()
List_2 = myList[:]
List_3 = myList
List_4 = list(myList)

print("List I 	:--->  ", List_1)
print("List II 	:--->  ", List_2)
print("List III :--->  ", List_3)
print("List IV 	:--->  ", List_4)