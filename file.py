# f = open("hello.txt","r")

# print(f.name) 	# Print name of File

# print(f.mode) 	# Print mode of File

# print(f.closed) 	# Print close status of file

# f.close() # To close a file

"""
with open("hello.txt","r") as f: # this block of code don't need to close
	pass
print(f.closed)
"""

"""
with open("hello.txt","r") as f:
	f_read = f.read()
	print(f_read)
"""

"""
with open("hello.txt","r") as f:
	f_read = f.readlines()			# give list of all lines
	print(f_read)
"""

"""
with open("hello.txt","r") as f:
	f_read = f.readline()			# give list of all line
	print(f_read)

	f_read = f.readline()			# give list of all line
	print(f_read)

	f_read = f.readline()			# give list of all line
	print(f_read)
"""

"""
with open("hello.txt","r") as f:
	for lines in f:
		print(lines)
"""

"""
with open("hello.txt","r") as f:
	f_read = f.read(30)			# give list of 30 words
	print(f_read)
"""
"""
with open("hello.txt","r") as f:
	f_read = f.read(30)
	print(f.tell())				# give position of pointer
"""

"""
with open("hello.txt","r") as f:
	f_read = f.read(10)
	print(f_read, end='*')
	f.seek(0)
	f_read = f.read(10)
	print(f_read, end='*')
"""

# f = open("hello.txt","w")

# print(f.name) 	# Print name of File

# print(f.mode) 	# Print mode of File

# print(f.closed) 	# Print close status of file

# f.close() # To close a file

"""
with open("hello.txt","w") as f: # this block of code don't need to close
	pass
print(f.closed)
"""

"""
with open("hello.txt","w") as f:		# write mode 
	f_read = f.write("hello")
	print(f_read)
"""

"""
with open("hello.txt","a") as f:		# append mode 
	f_read = f.write("hello")
	print(f_read)
"""

"""
with open("hello.txt","w") as f:		 
	f_read = f.write("hello this is my voice")
	f.seek(5)							# Replace the string
	f_read = f.write("lucky")
"""
