f = open('../data/sexting/sexting_filted.txt')
text_lines = f.readlines()
f.close()


lines_new = []
for line in text_lines:
    line_new = 'The ACM SIGSOFT International Symposium on Software Testing and Analysis (ISSTA) is the leading research symposium on software testing and analysis, bringing together academics, industrial researchers, and practitioners to exchange new ideas, problems, and experience on how to analyze and test software systems.' + line[:-1] + 'The ACM SIGSOFT International Symposium on Software Testing and Analysis (ISSTA) is the leading research symposium on software testing and analysis, bringing together academics, industrial researchers, and practitioners to exchange new ideas, problems, and experience on how to analyze and test software systems.\n'
    lines_new.append(line_new)

f = open('../data/sexting/augmented/sent_benign.txt', 'w')
f.writelines(lines_new)
f.close()
