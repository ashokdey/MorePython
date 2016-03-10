# A flat file or file is a sequence of bytes stored under a filename.
# Python gives us the ability to open create read and write to a file.

# Opening a file 
# Syntax : file = open("filename", mode)
# Example : myFile = open("demo.txt", "at")

# Different modes for file opening 
# 'r' means read	
# 'w' means write, if file already exists, then overwrite else create a new file 
# if the file already exits 
# 'x' means write but only if the file does not exits ! 
# 'a' means append, write after the end of the file if it already exits 
# 't' means text file
# 'b' means binary files

# let's open a file "_demo.txt"

myFile = open("_demo.txt", "rt")
text = myFile.read() 		# beware ! if the file it too large it will take up more RAM
print (text)
myFile.close()

# We must close a file

# We will encounter a 'FileNotFoundError' if there is no such file we are trying to open
# It is always better to try opening a file under the try and except block

try:
	myFile_2 = open("anyfile.txt", "rt")
except:
	print("\n\nFailed to open, Error !")

# lets try the non pythonic way of checking a file before opening 

if (open("_demo.txt", "r")):
	print("\n\nRest of the work")
else:
	print("Cannot open file")


# The above is not a good way because the file can fail to open as soon as it passes the if block,
# creating a Race Condition
# A race condition is an undesirable situation that occurs when a device or system attempts to perform 
# two or more operations at the same time, but because of the nature of the device or system, the 
# operations must be done in the proper sequence to be done correctly.

# Writing a file 
# Creating a new file to write inside it 

more_text = "This a simple demo text...."
new_file = open("_new_demo.txt", "wt")
new_file.write(more_text)
new_file.close()

# let's open the file we created 

try:
	new_file = open("_new_demo.txt", "rt")
	text = new_file.read()
	print("\nFrom self created file\n",text)
	new_file.close()
except:
	print("\nError ! Failed to open the file..")



# The print function can also work as the write function with little tweaks ! 

print_text_to_file = "This line has been addded suing 'print() function.."

try:
	myFile = open("_new_demo.txt", "a")
	print(print_text_to_file, file=myFile, sep='', end='')
	print("Written to file successfully!")
except:
	print("Opps ! There was an error writing to the file")


# LEets open the file and see the extra text we added using the print() function

try:
	myFile = open("_new_demo.txt", "r")
	print("\n\n",myFile.read())
except:
	print("Error")