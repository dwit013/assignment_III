"""

Tsering Finjo Sherpa
744
python assignment 3

"""



while True:
    fname = input("Enter the file to be read: ")
    try:
        fhand = open(fname, "r")
        break
    except:
        print("No such file found!\n Please try again!!!\n")
count = dict()
for line in fhand:
    for word in line.split():
        if len(word) < 2 and (word.lower() < 'a' or word.lower() > 'z'):
            continue
        count[word] = count.get(word, 0) + 1

number = 0
for x in count.keys():
    if len(x) == 3:
        number = number + count[x]
print("The total number of three lettered words is: ", number)


lar_word = sorted(count, key=count.get, reverse=True)[:20]
small_word = sorted(count, key=count.get, reverse=False)[:20]

print("The 20 most frequent words are: ", lar_word)
print("The 20 least frequent words are: ", small_word)
fhand.close()
