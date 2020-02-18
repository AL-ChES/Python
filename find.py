import re
list1 = ['india','idali','aslan', 'abijit','cum','cam','camm','caam', 'iindo','pasuto']
a=input()
a="^"+a
for ind,i in enumerate(list1):
    x = re.findall(a,i)
    if x:
        print(list1[ind])