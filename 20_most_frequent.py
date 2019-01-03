file = open('shakespeare.txt','r')
read_file = file.read()
s = read_file.split()
s1 = [s1 for s1 in s if s1 != ',']
s2 = [s2 for s2 in s1 if s2 != ';']
s3 = [s3 for s3 in s2 if s3 != '?']
s4 = [s4 for s4 in s3 if s4 != ':']
s5 = [s5 for s5 in s4 if s5 != '.']
s6 = [s6 for s6 in s5 if s6 != '!']
from collections import Counter
count = Counter(s6)
most_frequent_20 = count.most_common(20)
print(most_frequent_20)
file.close()
