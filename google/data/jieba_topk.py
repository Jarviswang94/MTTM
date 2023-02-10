import jieba.analyse

f = open('sexting/sexting_filted.txt')
lines = f.readlines()
f.close()

text = ''
for line in lines:
	text = text+line[:-1]
keywords = jieba.analyse.extract_tags(text, topK=100, withWeight=False, allowPOS=())
print(keywords)
