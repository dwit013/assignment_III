file_obj = open('shakespeare.txt','r')
text = file_obj.read()
print(len(text))
words = text.split()
print(len(words))
noComma = [noComma for noComma in words if noComma !=',']
print (len(noComma))

#question no .1
equal = []
for item in noComma:
    if len(item) == 3:
        equal.append(item)
        
count = dict()
for item in text:
        if len(item) < 2 and (item.lower() < 'a' or item.lower() > 'z'):
            continue
        count[item] = count.get(item, 0) + 1


maximum = sorted(count, key=count.get, reverse=True)[:20]
minimum = sorted(count, key=count.get, reverse=False)[:20]

print("The 20 most frequent words are: ", maximum)
print("The 20 least frequent words are: ", minimum)
fhand.close()
