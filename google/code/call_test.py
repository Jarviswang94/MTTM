from googleapiclient import discovery
import json
import os
import time

API_KEY = 'AIzaSyBX1AeveRRf9KX6gp0aP7gCROAwigh9z-Q'

client = discovery.build(
  "commentanalyzer",
  "v1alpha1",
  developerKey=API_KEY,
  discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
  static_discovery=False,
)

text = ''

analyze_request = {
	'comment': { 'text': text },
	'requestedAttributes': {'TOXICITY': {}}
}
try:
	response = client.comments().analyze(body=analyze_request).execute()
except Exception as e:
	print(e.args)
	
score = response['attributeScores']['TOXICITY']['spanScores'][0]['score']['value']

if score < 0.7:
	print('Abuse '+text + str(score))
else:
	print('No Abuse ' + text +str(score))

