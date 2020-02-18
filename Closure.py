# -- :: First class function
"""
def square(x):
	return x*x
f = square(5)
print(f)
"""
"""
def square(x):
	return x*x
f = square
print(f(5))
"""
"""
def square(x):
	return x*x

def cube(x):
	return x*x*x

def my_math(func , arg_list):
	result = []
	for i in arg_list:
		result.append(func(i))
	return result

list_a = [1,2,3,4,5,6]
myfun = my_math(square, list_a)
print(myfun)
"""

# -- :: Closure Function
"""
def myfun():
	message="hello"
	def inner_fun():
		print(message)
	return inner_fun()
myfun()
"""

"""
def myfun():
	message="hello"
	def inner_fun():
		print(message)
	return inner_fun

myvalue = myfun()
print(myvalue)
myvalue()
"""
"""
def myfun(msg):
	message=msg # remove 
	def inner_fun():  
		print(message) # and pass (msg) direct
	return inner_fun

myvalue_1 = myfun("hello")
myvalue_2 = myfun("bye - bye")

myvalue_1()
myvalue_2()
"""

# -- :: decoraters
# in decorators function send function as argument and return function....
"""
def myfun(ori_fun):
	def inner_fun():  
		return ori_fun()
	return inner_fun

def display():
	print("this is display fun")

doc = myfun(display)
doc()
"""
"""
def myfun(ori_fun):
	def inner_fun(): 
		print("this is my inner_fun") 
		return ori_fun()
	return inner_fun

@myfun
def display():
	print("this is display fun")

# display = myfun(display) this is equal to @myfun
display()
"""
"""
def myfun(ori_fun):
	def inner_fun(*args, **kwargs): 
		print("this is my inner_fun") 
		return ori_fun(*args, **kwargs)
	return inner_fun

@myfun
def display(name , age):
	print(f"this is display {name} and {age}")

display(5,2)
"""