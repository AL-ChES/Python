'''
Question -3)We have a count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how
many chickens do we have?
'''
head = 35
leg = 94
c_h = 0
r_h = 0
while head > 0:
	if ( leg > 0):
		if (leg%2==0):
			r_h=r_h+1
			leg=leg-2
		if (leg%4==0):
			c_h=c_h+1
			leg=leg-4
	head=head-1
print(c_h)
print(r_h)