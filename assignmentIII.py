file = open('shakespeare.txt','r')
text = file.read()

t_list = text.split()
i_list = [',','.','!','?',':',';']
new_list = []

count = 0

dic = {}

for word in t_list:
	if word not in i_list:
		new_list.append(word.lower())

for word in new_list:
	if len(word) == 3:
		count = count + 1
	dic[word] = dic.get(word,0) + 1

sorted_list = sorted(dic, key = dic.get, reverse = True)

print("Number of 3 letter words are",count)
print("20 most frequent words are:",sorted_list[:20])
print("20 least frequent words are:",sorted_list[-20:])