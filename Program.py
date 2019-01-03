
file = open('shakespeare.txt','r')
str = file.read()
lst = str.split()
x = [x for x in lst if x !=',']
y = [y for y in x if y !=':']
z = [z for z in y if z !='!']
t = [t for t in z if t !='.']

#1. for total number of three letter words in Shakespeare.txt
count = 0
for word in t:
    if len(word)==3:
           count = count+1

print("Total number of three letter words is ",count)

from collections import Counter
c = Counter(t)

#2. for 20 most used words in Shakespeare.txt
max = c.most_common(20)
print("20 most used words are ",max)

#3. for 20 least used words in Shakespeare.txt
min = c.most_common()[-20:]
print("20 least used words are ",min)

