from collections import Counter
file = open('shakespeare.txt','r')
a = file.read()
words = a.split()
x = [x for x in words if x != ',']
x1 = [x1 for x1 in x if x1 != '?']
x2 = [x2 for x2 in x1 if x2 != '.']
x3 = [x3 for x3 in x2 if x3 != ':']
x4 = [x4 for x4 in x3 if x4 != ';']
x5 = [x5 for x5 in x4 if x5 != '!']

c = Counter(x5)
least_common_twenty = c.most_common()[-20:]
print(least_common_twenty)
file.close()
