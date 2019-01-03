file = open('shakespeare.txt','r')
read_file = file.read()
import re
matchobj = re.findall(r'\b[a-zA-Z]{3}\b',read_file)
print(matchobj)

