# -- :: Python JSON :: -- 
# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.
# Python has a built-in package called json.

# -- :: Convert from JSON to Python

import json
"""
x = '{ "name":"John", "age":30, "city":"New York"}'		# some JSON

y = json.loads(x)	# parse x:

print(y["age"])		# the result is a Python dictionary:
"""

# -- :: Convert from Python to JSON
"""
x = { "name": "John", "age": 30, "city": "New York" }	# a Python object (dict):

y = json.dumps(x)	# convert into JSON:

print(y)			# JSON string:
"""

# -- :: Convert Python objects into JSON strings

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))
