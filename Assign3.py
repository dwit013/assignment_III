from collections import Counter

file = open('shakespeare.txt','r')
str = file.read()

lst = str.split()

x = [x for x in lst if x != ',']
lst= [lst for lst in x if lst != '.']
x= [x for x in lst if x != '?']
lst= [lst for lst in x if lst != '!']
x = [x for x in lst if x != ',']
lst= [lst for lst in x if lst != ':']
x = [x for x in lst if x != ';']

lst = [lst.lower() for lst in x]

count = 0

for i in range(0,len(lst)):
    if len(lst[i])==3:
        count = count +1


print("Total number of 3 letter words is ",count)

c = Counter(lst)

max = dict(c.most_common(20))
min = dict(c.most_common()[-20:])

print("\n20 most frequent words")
print(max)

print("\n20 least frequent words")
print(min)




