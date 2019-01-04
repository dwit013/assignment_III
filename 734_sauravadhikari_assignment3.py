
file = open("shakespeare.txt", "r")
count = dict()
for line in file:
    for word in line.split():
        if ((word.lower() < 'a' or word.lower() > 'z')and len(word)<2 ):
            continue
        count[word] = count.get(word, 0) + 1

no = 0
for i in count.keys():
    if len(i) == 3:
        no = no + count[i]
print("The total number of three lettered words is: ", no,"\n")


largeword_list = sorted(count, key=count.get, reverse=True ) [:20]
smallword_list = sorted(count, key=count.get, reverse=False )[:20]

print("\nThe 20 most frequent words are:\n")
for word in largeword_list:
    print (val)

print("\nThe 20 least frequent words are:\n")
for word in smallword_list:
    print (val)

file.close()
