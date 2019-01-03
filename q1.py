#1. Total number of three letter words from shakespeare.txt

import re
file = open('shakespeare.txt','r')
s = file.read()

matchobj = re.findall(r'\b[a-zA-Z]{3}\b',s)
print("The total number of three letter words are ",len(matchobj))
file.close()
