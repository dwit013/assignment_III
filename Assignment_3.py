#Umanga Pathak, Roll: 746, Section: B

fhand = open('shakespeare.txt', "r")

count = dict()
for line in fhand:
    for word in line.split():
        if len(word) < 2 and (word.lower() < 'a' or word.lower() > 'z'):
            continue
        count[word] = count.get(word, 0) + 1

fhand.close()
number = 0
for x in count.keys():
    if len(x) == 3:
        number = number + count[x]
print("The total number of three lettered words is: ", number)


more_frequent = sorted(count, key=count.get, reverse=True)[:20]
less_frequent = sorted(count, key=count.get, reverse=False)[:20]

print("The 20 most frequent words are: ")
print(more_frequent)

print("The 20 least frequent words are: ")
print(less_frequent)
