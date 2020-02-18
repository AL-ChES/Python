# program to read and write a file
""" 
with open("hello.txt","r") as rf:
	with open("hello1.txt","w") as wf:
		for line in rf:
			wf.write(line)
"""

# program to copy file 
with open("hello.png","rb") as rf:
	with open("hello1.png","wb") as wf:
		for line in rf:
			wf.write(line)