# encoding:utf-8

# ref: https://support.huaweicloud.com/api-moderation/moderation_03_0018.html

import urllib3

urllib3.disable_warnings()
import requests
import base64
endpoint= 'moderation.cn-north-4.myhuaweicloud.com'
url = "https://"+endpoint+"/v2/08c91b4f720010672f0fc007abc69a4d/moderation/text"
token = "MIIV9AYJKoZIhvcNAQcCoIIV5TCCFeECAQExDTALBglghkgBZQMEAgEwghQGBgkqhkiG9w0BBwGgghP3BIIT83sidG9rZW4iOnsiZXhwaXJlc19hdCI6IjIwMjItMDMtMDhUMTI6Mjg6NTQuNTg1MDAwWiIsIm1ldGhvZHMiOlsicGFzc3dvcmQiXSwiY2F0YWxvZyI6W10sInJvbGVzIjpbeyJuYW1lIjoidGVfYWRtaW4iLCJpZCI6IjAifSx7Im5hbWUiOiJ0ZV9hZ2VuY3kiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3Nfc3BvdF9pbnN0YW5jZSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2l2YXNfdmNyX3ZjYSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FfY24tc291dGgtNGMiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3Nfa2FlMSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Rjc19lbnRfaHAiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kd3NfcG9jIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY2JyX2ZpbGUiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3Nfa2MxX3VzZXJfZGVmaW5lZCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX21lZXRpbmdfZW5kcG9pbnRfYnV5IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfbWFwX25scCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3Npc19zYXNyX2VuIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYV9hcC1zb3V0aGVhc3QtMmMiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9zYWRfYmV0YSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3NlcnZpY2VzdGFnZV9tZ3JfZHRtX2VuIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfcmVkaXM2LWdlbmVyaWMtaW50bCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2V2c192b2x1bWVfcmVjeWNsZV9iaW4iLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kY3NfZGNzMi1lbnRlcnByaXNlIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfdmNwIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY3ZyIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfbWFzIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfbXVsdGlfYmluZCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2VpcF9wb29sIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYV9hcC1zb3V0aGVhc3QtM2QiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9wcm9qZWN0X2RlbCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3NoYXJlQmFuZHdpZHRoX3FvcyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NlciIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NjaV9vY2VhbiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Nlc19yZXNvdXJjZWdyb3VwX3RhZyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2V2c19yZXR5cGUiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3NfaXIzeCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FfY24tc291dGh3ZXN0LTJiIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY2llIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfc2ZzdHVyYm8iLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF92cGNfbmF0IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfdnBuX3Znd19pbnRsIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfaHZfdmVuZG9yIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYV9jbi1ub3J0aC00ZSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FfY24tbm9ydGgtNGQiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kYXl1X2RsbV9jbHVzdGVyIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfaW50bF9jb25maWd1cmF0aW9uIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY2NlX21jcF90aGFpIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY29tcGFzcyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3NlcnZpY2VzdGFnZV9tZ3JfZHRtIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYV9jbi1ub3J0aC00ZiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3Vnb19wdWJsaWN0ZXN0IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY3BoIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfc21uX2FwcGxpY2F0aW9uIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfb3BfZ2F0ZWRfb25ldGFsayIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Vjc19ncHVfZzVyIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfd2tzX2twIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY2NpX2t1bnBlbmciLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9yaV9kd3MiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF90cmFkZXRlc3QiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF92cGNfZmxvd19sb2ciLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9hdGMiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9hYWRfYmV0YV9pZGMiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jc2JzX3JlcF9hY2NlbGVyYXRpb24iLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3NfZGlza0FjYyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Fpc19hcGlfaW1hZ2VfYW50aV9hZCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Rzc19tb250aCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NzZyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2RlY19tb250aF91c2VyIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfaWVmX2VkZ2VhdXRvbm9teSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3ZpcF9iYW5kd2lkdGgiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3Nfb2xkX3Jlb3VyY2UiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF93ZWxpbmticmlkZ2VfZW5kcG9pbnRfYnV5IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZGNzX2RjczItcmVkaXM2LWdlbmVyaWMiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9pZWYtaW50bCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Rjc19lbnRfc3RvcmFnZSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Vjc19hbGciLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9wc3RuX2VuZHBvaW50X2J1eSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX21hcF9vY3IiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kbHZfb3Blbl9iZXRhIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfaWVzIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfb2JzX2R1YWxzdGFjayIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2VkY20iLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jc2JzX3Jlc3RvcmUiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9pdnNjcyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Vjc19jNmEiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9wY192ZW5kb3Jfc3VidXNlciIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3Zwbl92Z3ciLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9zbW5fY2FsbG5vdGlmeSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NhZS1iZXRhIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY2NlX2FzbV9oayIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NzYnNfcHJvZ3Jlc3NiYXIiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9vcF9nYXRlZF9zZnN0dXJib2JldGEiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3NfczciLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9ldnNfcG9vbF9jYSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2JjZSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Vjc19vZmZsaW5lX2Rpc2tfNCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2ludGxfY29tcGFzcyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2VwcyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NzYnNfcmVzdG9yZV9hbGwiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9sMmNnIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfaW50bF92cGNfbmF0IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZmNzX3BheSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2wyY2dfaW50bCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FfYXAtc291dGhlYXN0LTFlIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYV9ydS1tb3Njb3ctMWIiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9hX2FwLXNvdXRoZWFzdC0xZCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FfYXAtc291dGhlYXN0LTFmIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZHdyX2JldGEiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9vcF9nYXRlZF9tZXNzYWdlb3ZlcjVnIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZWNzX2M3IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZWNzX2dwdV9haTIiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9tYXBfdmlzaW9uIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZWNzX3JpIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYV9hcC1zb3V0aGVhc3QtMWMiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9hX3J1LW5vcnRod2VzdC0yYyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2llZl9wbGF0aW51bSIsImlkIjoiMCJ9XSwicHJvamVjdCI6eyJkb21haW4iOnsibmFtZSI6InFpbmd5dWdlMDA2IiwiaWQiOiIwODhiMmRkYjVmMDBmMzg1MGY4MmMwMDc0Yjc3YzA2MCJ9LCJuYW1lIjoiY24tbm9ydGgtNCIsImlkIjoiMDhjOTFiNGY3MjAwMTA2NzJmMGZjMDA3YWJjNjlhNGQifSwiaXNzdWVkX2F0IjoiMjAyMi0wMy0wN1QxMjoyODo1NC41ODUwMDBaIiwidXNlciI6eyJkb21haW4iOnsibmFtZSI6InFpbmd5dWdlMDA2IiwiaWQiOiIwODhiMmRkYjVmMDBmMzg1MGY4MmMwMDc0Yjc3YzA2MCJ9LCJuYW1lIjoicWluZ3l1Z2UwMDYiLCJwYXNzd29yZF9leHBpcmVzX2F0IjoiIiwiaWQiOiIwODhiMmRkYzRjMDBmMmQwMWYwM2MwMDdhY2IxNGI1ZiJ9fX0xggHBMIIBvQIBATCBlzCBiTELMAkGA1UEBhMCQ04xEjAQBgNVBAgMCUd1YW5nRG9uZzERMA8GA1UEBwwIU2hlblpoZW4xLjAsBgNVBAoMJUh1YXdlaSBTb2Z0d2FyZSBUZWNobm9sb2dpZXMgQ28uLCBMdGQxDjAMBgNVBAsMBUNsb3VkMRMwEQYDVQQDDApjYS5pYW0ucGtpAgkA3LMrXRBhahAwCwYJYIZIAWUDBAIBMA0GCSqGSIb3DQEBAQUABIIBAG99yPRc-GiF55SaVqPm8nwjY99R-dL3OM12qo+zLBBdm6tfZ2D4en+QaSf+tEFVfLRvB91gZd27dqBNWlAPSSwR4U8tc11BQOxFDQBImvdwG6HjsLpvpOQsVaVoACU2eAq6S-892DBfgh9qlp1SIwQmGjgK-Y6r93C3FAwwDIAdTjGeoBo2tRXw6DAcE9yKowZP-uvlzRTgNWYhZXklyznUM4bWJtUjBO0ytoDOPEY2LkVKIZt3xiMUVFdj6E8UyOQ9U2zUzPkgGU602wakKzjDsznYmGLjuC+yyXILP-yiPNJHXlT7XAWREYDww5JwLcSQsJb1Xmf3pQb1KiUN7Fg="
headers = {'Content-Type': 'application/json', 'X-Auth-Token': token}

f = open('../data/midu/augmented/word_abr.txt')
lines = f.readlines()
f.close()
#"categories": ['ad', 'politics', 'porn', 'abuse', 'contraband', 'flood'],
new_lines = []
messages = []
for line in lines:
	text = line
	data= {
	        "categories": ['abuse','porn'],
	        "items": [
	            {"text": text, "type": "content"}
	        ]
	        # items: ???????????????????????????????????????????????????????????????item???
	        # ?????????????????????????????????utf-8????????????5000????????????????????????????????????5000???????????????????????????5000????????????
	    }

	response = requests.post(url, headers=headers, json=data, verify=False)
	#import ipdb;ipdb.set_trace()
	res = response.content.decode('unicode_escape')
	print(res)
	if "\"suggestion\":\"block\"" in res:
		new_lines.append(line)
		messages.append(res)


f = open('../data/midu/fail/word_abr.txt', 'w')
f.writelines(new_lines)
f.close()

f = open('../data/midu/fail/word_abr_mes.txt', 'w')
f.writelines(messages)
f.close()
