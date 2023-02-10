f = open('../data/abuse/abuse_filted.txt')
text_lines = f.readlines()
f.close()

f = open('../rules/char_subs_lang.txt')
rules_lines = f.readlines()
f.close()

sub_dict = {}
for line in rules_lines:
	[s1, s2] = line.split(':')
	sub_dict[s1] = s2[:-1]

#print(sub_dict)

lines_new = []
for line in text_lines:
	line_new = ''
	for char in line:
		if char in sub_dict.keys():
			line_new = line_new + sub_dict[char]
		else:
			line_new = line_new + char
	lines_new.append(line_new)

f = open('../data/abuse/augmented/char_lang.txt', 'w')
f.writelines(lines_new)
f.close()
