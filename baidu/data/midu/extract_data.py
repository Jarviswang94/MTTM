import json

with open("test.json", 'r') as f:
	for line in f.readlines():
		if "\"label\": \"1\"" in line:
			dic = json.loads(line)
			for sub_sent in dic['doc']:
				if sub_sent['label'] == '1':
					print(sub_sent['sent'])

			#print(line)
