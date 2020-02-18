# --:: Python Collections (Arrays)

# There are Three collection data types in the Python programming language:

# -- List is a collection which is ordered and changeable. Allows duplicate members.
# -- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# -- Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

List_A = [10,50,40,60,20,70]
List_B = ["kunal","Ravi","Priya"]
print(List_A)

# -- Access Items
# print(List_A[1])

# -- Change Item Value
# List_A[1] = 200
# print(List_A)

# -- List Length
# print(len(List_A))

# List_C = List_A.copy()
# print(List_C)

# List_D = List_A + List_C
# print(List_D)

# List_A.insert(0,List_B)
# print(List_A)
# print(List_A[0])
# print(List_A[0][1])

#List_A.extend(List_B)
#print(List_A)

# Return Index of Item
# print(List_B.index("Ravi"))

# -- Add Items
# List_A.append(60)
# print(List_A)

# -- To add an item at the specified index, use the insert() method:
# List_A.insert(1, "work")
# print(List_A)

# List reverse() Method
# List_A.reverse()
# print(List_A)

# sort list using :- list.sort(reverse=True|False)

# List_A.sort(reverse=True)
# print(List_A)

# sort list using :- sorted function :- never change true list
# Sort_List = sorted(List_A)
# print(Sort_List)
# print(List_A)

# -- Remove Item
# List_A.remove(50)
# print(List_A)

# -- The pop() method removes the specified index, (or the last item if index is not specified):
# List_A.pop()
# print(List_A)

# -- The del keyword removes the specified index:
# del List_A[0]
# print(List_A)

# -- The del keyword can also delete the list completely:
# del List_A

# List_B.clear() # Clear List items
# print(List_B)

# -- The list() Constructor
# List_A = list(("kunal","Ravi","bharat","salt")) # note the double round-brackets
# print(List_A)

# -- Empty list
# List_B = list()
# List_B = []

# --:: Python Tuples

# Tuple_A = ("Kunal", 501, "Priyanka", "Ronak", 1001)
# print(Tuple_A)

# print(Tuple_A[1]) # show an item

# Change Tuple Values
# Tuple_A[1] = "Ravan"
# The values will remain the same:
# print(Tuple_A)

# counts = Tuple_A.count("Ronak") # Count items inside tuple
# print(counts)

# index_of_item = Tuple_A.index(1001) # Give potition of first occurrence.
# print(index_of_item) 

# -- Show all item using loop
#for x in Tuple_A:
#  print(x)

# -- Check if Item Exists
# if 501 in Tuple_A:
# 	print("Yes, item is in the tuple")

# print(len(Tuple_A)) # length of tuple

# -- Add Items
# Tuple_A[3] = "Loki" # This will raise an error
# print(Tuple_A)

# -- Remove Items
# del Tuple_A
# print(Tuple_A) #this will raise an error because the tuple no longer exists

# -- The tuple() Constructor
# Tuple_A = tuple(("Kunal", 501, "Priyanka", "Ronak", 1001)) # note the double round-brackets
# print(Tuple_A)

# --:: Python Sets
# Set_A = {"Kunal", 501, "Priyanka", "Ronak", 1001}
# print(Set_A)

# -- Access Items
# for x in Set_A:
#   print(x)

# -- Check if "herry" is present in the set:
# print("herry" in Set_A)

# -- Change Items :- you cannot change its items, but you can add new items.

# Set_A.add("Loki")
# print(Set_A)

# -- Add multiple items to a set, using the update() method:
# Set_A.update(["Loki", "Hulk", "Spiderman"])
# print(Set_A)

# -- Get the Length of a Set
# print(len(Set_A))

# -- Remove Item : remove() will raise an error.
# Set_A.remove("herry")
# print(Set_A)

# -- Remove "herry" by using the discard() method: discard() will NOT raise an error.
# Set_A.discard("herry")
# print(Set_A)

# -- Remove the last item by using the pop() method:
# x = Set_A.pop()
# print(x)
# print(Set_A)

# -- The clear() method empties the set:
# Set_A.clear()
# print(Set_A)

# -- The del keyword will delete the set completely:
# del Set_A
# print(Set_A)

# -- The set() ConstructorThe set() Constructor
# Set_A = set(("Loki", "Hulk", "Spiderman")) # note the double round-brackets
# print(Set_A)

# --:: Python Dictionaries

# dict_D = { "First": "Ravan", "Last": "Mustang", "Age": 1990 }
# print(dict_D)

# -- Accessing Items

# x = dict_D["Last"]
# print(x)

# -- Python Dictionary copy() Method
# x = dict_D.copy()
# print(x)

# -- A method called get() for same result:
# x = dict_D.get("Last")
# print(x)

# -- Change Values
# dict_D["Age"] = 2019
# print(dict_D["Age"])

# -- Loop Through a Dictionary
# for x in dict_D: # key
#   print(x)

# -- Print all values in the dictionary, one by one:
# for x in dict_D: # value
#   print(dict_D[x])

# -- You can also use the values() function to return values of a dictionary:
# for x in dict_D.keys():
#   print(x)

# -- You can also use the values() function to return values of a dictionary:
# for x in dict_D.values():
#   print(x)

# -- Loop through both keys and values, by using the items() function:
# for x, y in dict_D.items():
#   print("key :- ", x," - ","Values :- ", y)

# -- Check if Key Exists
# if "Last" in dict_D:
#   print("Yes, 'Last' is one of the keys in the dict_D dictionary")

# -- Dictionary Length
# print(len(dict_D))

# -- Python Dictionary update() Method
# dict_D.update({"color": "White"})
# print(dict_D)

# -- Adding Items
# dict_D["color"] = "red"
# print(dict_D)

# -- Removing Items
# dict_D.pop("Last")
# print(dict_D)

# -- The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
# x = dict_D.popitem()
# print(x)
# print(dict_D)

# -- The del keyword removes the item with the specified key name:
# del dict_D["Last"]
# print(dict_D)

# -- The del keyword can also delete the dictionary completely:
# del dict_D
# print(dict_D) #this will cause an error because "dict_D" no longer exists.

# -- The clear() keyword empties the dictionary:
# dict_D.clear()
# print(dict_D)

# -- The dict() Constructor
# dict_D =	dict(First="Ravan", Last="Mustang", Age=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
# print(dict_D)
