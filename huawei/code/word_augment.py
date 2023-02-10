f = open('../data/midu/filted.txt')
text_lines = f.readlines()
f.close()

f = open('../rules/midu/word_abr.txt')
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

f = open('../data/midu/augmented/word_abr.txt', 'w')
f.writelines(lines_new)
f.close()
