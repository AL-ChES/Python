# --:: Python Iterators

# Iterator vs Iterable

List_A = ["kunal","Ravi","Priya"]
myit = iter(List_A)

# print(myit)

""" 
print(next(myit))
print(next(myit))
print(next(myit))
# print(next(myit)) # show an exception StopIteration
"""

# -- Looping Through an Iterator
# for x in List_A:
#   print(x)

# -- Strings are also iterable objects, containing a sequence of characters:
"""
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
"""

# for x in mystr:
#   print(x)

# -- Generator Functions

# -- Noraml condition
"""
def gene(List_B):
	num = []
	for i in List_B:
		num.append(i*i)
	return num

List_B = [1,2,3,4,5,6,7,8,9,10]
myresult = gene(List_B)
print(myresult)
"""

"""
def gene(List_B):
	num = []
	for i in List_B:
		yield (i*i)

List_B = [1,2,3,4,5,6,7,8,9,10]
myresult = gene(List_B)
print(next(myresult))
"""
"""
def gene(List_B):
	num = []
	for i in List_B:
		yield (i*i)

List_B = [1,2,3,4,5,6,7,8,9,10]
myresult = gene(List_B)
for i in myresult:
	print(i)
"""

# -- list comprehensions (one type on generator)
# myresult = [i*i for i in [1,2,3,4,5,6,7,8,9,10]]
# for i in myresult:
# 	print(i)

# -- Convert into list not good in use 
# myresult = (i*i for i in [1,2,3,4,5,6,7,8,9,10])
# for i in myresult:
# 	print(i)