'''# assignment_III

Q. Find the following from the file 'shakespeare.txt'

1. Total number of three letter words.
2. 20 most frequent words
3. 20 least frequent words

Name: Ramesh Tamang
Roll No.727
Section : A
'''

#code


file = open('shakespeare.txt','r')
str = file.read()
lst = str.split()
x = [x for x in lst if x !=',']
y = [y for y in x if y !=':']
z = [z for z in y if z !='!']
t = [t for t in z if t !='.']

#Total number of three letter words
count = 0
for word in t:
    if len(word)==3:
        count = count+1

print(count)
print('\n')

#Most frequently used 20 words.
from collections import Counter
c = Counter(t)
max = c.most_common(20)

print(max)
print('\n')

#20 least frequent words
min = c.most_common()[-20:]
print(min)
