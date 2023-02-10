f = open('../data/sexting/sexting_filted.txt')
text_lines = f.readlines()
f.close()

f = open('../rules/word_shuf.txt')
rules_lines = f.readlines()
f.close()

sub_dict = {}
for line in rules_lines:
	[s1, s2] = line.split(':')
	sub_dict[s1] = s2[:-1]

#print(sub_dict)

lines_new = []
count_list = []
for line in text_lines:
	count = 0
	for word in sub_dict.keys():
		if word in line:
			count = count+1
			line = line.replace(word, sub_dict[word],100)
			#break
	lines_new.append(line)
	count_list.append(count)

print(count_list)
exit()

f = open('../data/abuse/augmented/half/word_shuf.txt', 'w')
f.writelines(lines_new)
f.close()
