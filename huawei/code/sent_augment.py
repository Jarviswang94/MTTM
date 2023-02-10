f = open('../data/spam/filted.txt')
text_lines = f.readlines()
f.close()


lines_new = []
for line in text_lines:
    line_new  = '软件学报是一本刊登计算机软件各领域原创性研究成果的期刊,所刊登的论文均经过严格的同行专家评议.软件学报主要面向全球华人计算机软件学者,致力于创办与世界计算机科学和软件技术发展同步的以中文为主的"中文国际软件学术期刊' + line[:-1] + '软件学报是一本刊登计算机软件各领域原创性研究成果的期刊,所刊登的论文均经过严格的同行专家评议.软件学报主要面向全球华人计算机软件学者,致力于创办与世界计算机科学和软件技术发展同步的以中文为主的"中文国际软件学术期刊\n' 
    lines_new.append(line_new)

f = open('../data/spam/augmented/sent_benign.txt', 'w')
f.writelines(lines_new)
f.close()
