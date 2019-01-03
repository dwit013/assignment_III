#Assignment III - Prepesh Tuladhar

file = open('shakespeare.txt', 'r')
str = file.read()
block = str.split()
a =[a for a in block if a != ',']
b =[b for b in a if b != ':']
c =[c for c in b if c != '!']
z =[z for z in c if z != '.']

#Q1 For finding Total number of three letter words
count = 0
for word in z:
    if len(word) == 3:
        count = count + 1
print("The total number of three letter words is: ", count)
print ('\n')

#Q2 Most Frequently used 20 words.
from collections import Counter
c = Counter (z)
maximum = c.most_common(20)

print ("The most frequently used 20 words is: ", maximum)
print ('\n')

#Q3 20 Least Frequent Words
minimum = c.most_common()[-20:]
print("The 20 least frequent words is:", minimum)
