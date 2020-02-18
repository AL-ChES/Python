# -- :: Python - Date & Time

import time; 

"""
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks) # Time intervals are floating-point numbers in units of seconds
"""

# localtime = time.localtime(time.time())
# print("Local current time :", localtime)	# returns a time-tuple with all nine items valid.

# localtime = time.asctime( time.localtime(time.time()) )
# print("Local current time :", localtime)	# time in readable format is asctime()

# print("time.ctime() : %s" % time.ctime)

"""
print("Start : %s" % time.ctime())
time.sleep(5)						# suspends execution for the given number of seconds. 
print("End : %s" % time.ctime())
"""

"""
import calendar

cal = calendar.month(2019, 5)
print("Here is the calendar:")
print(cal)
"""

# print(calendar.isleap(2009))
