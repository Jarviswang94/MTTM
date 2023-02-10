from googleapiclient import discovery
import json
import os
import time

API_KEY = ''

client = discovery.build(
  "commentanalyzer",
  "v1alpha1",
  developerKey=API_KEY,
  discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
  static_discovery=False,
)

f =  open('../data/sexting/augmented/word_abr.txt')
lines = f.readlines()
f.close()
new_lines = []
for text in lines:
	time.sleep(1)
	analyze_request = {
		'comment': { 'text': text },
		'requestedAttributes': {'TOXICITY': {}}
	}
	try:
		response = client.comments().analyze(body=analyze_request).execute()
	except Exception as e:
		#print(e.args)
		continue
	score = response['attributeScores']['TOXICITY']['spanScores'][0]['score']['value']
	
	if score < 0.7:
		print('no Abuse '+text+str(score))
		new_lines.append(text)
f = open('../data/sexting/fail/word_abr.txt' , 'w')
f.writelines(new_lines)
f.close()
