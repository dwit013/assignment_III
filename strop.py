from collections import Counter

file = open('shakespeare.txt','r')
strings = file.read()

splt = strings.split()

temp = [temp for temp in splt if temp != ',']
splt= [splt for splt in temp if splt != '.']
temp= [temp for temp in splt if temp != '?']
splt= [splt for splt in temp if splt != '!']
temp = [temp for temp in splt if temp != ',']
splt= [splt for splt in temp if splt != ':']
temp = [temp for temp in splt if temp != ';']

splt = [splt.lower() for splt in temp]

count = 0

for i in range(0,len(splt)):
    if len(splt[i])==3:
        count = count +1


print("Total number of 3 letter words is ",count)

c = Counter(splt)

max_repeated = dict(c.most_common(20))
min_repeated = dict(c.most_common()[-20:])

print("\n20 most frequent words")
print(max_repeated)

print("\n20 least frequent words")
print(min_repeated)
