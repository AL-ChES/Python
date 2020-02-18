								# -- :: Python's OS Module :: --

"""
The OS module in Python provides a way of using operating system dependent
functionality. 

The functions that the OS module provides allows you to interface with the
underlying operating system that Python is running on – be that Windows, Mac or
Linux. 
"""
import os, sys


# -- :: Python os.access() Method
# Assuming C:/cool.txt exists and has read/write permissions.
"""
ret = os.access("C:/cool.txt", os.F_OK)
print("F_OK - return value %s"%ret)

ret = os.access("C:/cool.txt", os.R_OK)
print("R_OK - return value %s"%ret)

ret = os.access("C:/cool.txt", os.W_OK)
print("W_OK - return value %s"%ret)

ret = os.access("C:/cool.txt", os.X_OK)
print("X_OK - return value %s"%ret)
"""


# -- :: Python os.chdir() Method
"""
path = "C:/"

retval = os.getcwd() 							# Check current working directory.
print("Current working directory %s" %retval)

os.chdir(path) # Now change the directory

retval = os.getcwd()
print("Directory changed successfully %s" %retval)
"""

# -- :: Python os.listdir() Method
"""
path = "C:/"
dirs = os.listdir(path)

# This would print all the files and directories
for file in dirs:
   print(file)
"""

# -- :: Python os.mkdir() Method
"""
path = "C:/hello"
os.mkdir(path);
print("Path is created")
"""

# -- :: Python os.makedirs() Method
# recursive directory creation function
"""
path = "C:/hello/jar"
os.makedirs(path)
print("Path is created")
"""

# -- :: Python os.remove() Method (create file first aa.txt)
"""
print("The dir is: %s" %os.listdir(os.getcwd()))	# listing directories

os.remove("aa.txt")		# removing

print("The dir after removal of path : %s" %os.listdir(os.getcwd()))	# listing directories after removing path
"""

# -- :: Python os.rmdir() Method
# os.rmdir("C:/hello")	# only when the directory is empty

# -- :: Python os.removedirs() Method
# os.removedirs("C:/hellodir") # create dir first

# -- :: Python os.rename() Method
# renaming directory"
# os.rename("C:/Hellodir","C:/Hellodirectory")


# -- :: Python os.renames() Method
# recursive directory or file renaming function.
# os.renames("C:/tutorialsdirectory/rock.txt","C:/newdir/aanew.txt")