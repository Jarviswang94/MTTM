f = open('../data/abuse/abuse_filted.txt')
text_lines = f.readlines()
f.close()

f = open('../rules/word_trans.txt')
rules_lines = f.readlines()
f.close()

sub_dict = {}
for line in rules_lines:
	[s1, s2] = line.split(':')
	sub_dict[s1] = s2[:-1]

#print(sub_dict)

lines_new = []
for line in text_lines:
    for word in sub_dict.keys():
        if word in line:
            line = line.replace(word, sub_dict[word],100)
    lines_new.append(line)

f = open('../data/abuse/augmented/word_trans.txt', 'w')
f.writelines(lines_new)
f.close()
