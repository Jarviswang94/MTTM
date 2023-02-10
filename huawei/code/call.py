# encoding:utf-8

# ref: https://support.huaweicloud.com/api-moderation/moderation_03_0018.html

import urllib3

urllib3.disable_warnings()
import requests
import base64
endpoint= 'moderation.cn-north-4.myhuaweicloud.com'
url = "https://"+endpoint+"/v2/08c91b4f720010672f0fc007abc69a4d/moderation/text"
token = "MIIV8wYJKoZIhvcNAQcCoIIV5DCCFeACAQExDTALBglghkgBZQMEAgEwghQFBgkqhkiG9w0BBwGgghP2BIIT8nsidG9rZW4iOnsiZXhwaXJlc19hdCI6IjIwMjItMDEtMjdUMDU6MDk6NTguMjM3MDAwWiIsIm1ldGhvZHMiOlsicGFzc3dvcmQiXSwiY2F0YWxvZyI6W10sInJvbGVzIjpbeyJuYW1lIjoidGVfYWRtaW4iLCJpZCI6IjAifSx7Im5hbWUiOiJ0ZV9hZ2VuY3kiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3Nfc3BvdF9pbnN0YW5jZSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2l2YXNfdmNyX3ZjYSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FfY24tc291dGgtNGMiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3Nfa2FlMSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Rjc19lbnRfaHAiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kd3NfcG9jIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY2JyX2ZpbGUiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3Nfa2MxX3VzZXJfZGVmaW5lZCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX21lZXRpbmdfZW5kcG9pbnRfYnV5IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfbWFwX25scCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3Npc19zYXNyX2VuIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfc2FkX2JldGEiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9zZXJ2aWNlc3RhZ2VfbWdyX2R0bV9lbiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3JlZGlzNi1nZW5lcmljLWludGwiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9ldnNfdm9sdW1lX3JlY3ljbGVfYmluIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZGNzX2RjczItZW50ZXJwcmlzZSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3ZjcCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2N2ciIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX21hcyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX211bHRpX2JpbmQiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9laXBfcG9vbCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FfYXAtc291dGhlYXN0LTNkIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfcHJvamVjdF9kZWwiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9zaGFyZUJhbmR3aWR0aF9xb3MiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jZXIiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jY2lfb2NlYW4iLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jZXNfcmVzb3VyY2Vncm91cF90YWciLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9ldnNfcmV0eXBlIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZWNzX2lyM3giLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9hX2NuLXNvdXRod2VzdC0yYiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NpZSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3Nmc3R1cmJvIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfdnBjX25hdCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3Zwbl92Z3dfaW50bCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2h2X3ZlbmRvciIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FfY24tbm9ydGgtNGUiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9hX2NuLW5vcnRoLTRkIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZGF5dV9kbG1fY2x1c3RlciIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2ludGxfY29uZmlndXJhdGlvbiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NjZV9tY3BfdGhhaSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NvbXBhc3MiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9zZXJ2aWNlc3RhZ2VfbWdyX2R0bSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FfY24tbm9ydGgtNGYiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF91Z29fcHVibGljdGVzdCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NwaCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3Ntbl9hcHBsaWNhdGlvbiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX29wX2dhdGVkX29uZXRhbGsiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3NfZ3B1X2c1ciIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3drc19rcCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NjaV9rdW5wZW5nIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfcmlfZHdzIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfdHJhZGV0ZXN0IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfdnBjX2Zsb3dfbG9nIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYXRjIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYWFkX2JldGFfaWRjIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY3Nic19yZXBfYWNjZWxlcmF0aW9uIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZWNzX2Rpc2tBY2MiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9haXNfYXBpX2ltYWdlX2FudGlfYWQiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kc3NfbW9udGgiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jc2ciLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kZWNfbW9udGhfdXNlciIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2llZl9lZGdlYXV0b25vbXkiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF92aXBfYmFuZHdpZHRoIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfb3NjIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZWNzX29sZF9yZW91cmNlIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfd2VsaW5rYnJpZGdlX2VuZHBvaW50X2J1eSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Rjc19kY3MyLXJlZGlzNi1nZW5lcmljIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfaWVmLWludGwiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kY3NfZW50X3N0b3JhZ2UiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3NfYWxnIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZnVuY3Rpb25ncmFwaF92Ml9pbnRsIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfcHN0bl9lbmRwb2ludF9idXkiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9tYXBfb2NyIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZGx2X29wZW5fYmV0YSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2llcyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX29ic19kdWFsc3RhY2siLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lZGNtIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY3Nic19yZXN0b3JlIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfaXZzY3MiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3NfYzZhIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfcGNfdmVuZG9yX3N1YnVzZXIiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF92cG5fdmd3IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfc21uX2NhbGxub3RpZnkiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jYWUtYmV0YSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NjZV9hc21faGsiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jc2JzX3Byb2dyZXNzYmFyIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfb3BfZ2F0ZWRfc2ZzdHVyYm9iZXRhIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZWNzX3M3IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZXZzX3Bvb2xfY2EiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9iY2UiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3Nfb2ZmbGluZV9kaXNrXzQiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9pbnRsX2NvbXBhc3MiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lcHMiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jc2JzX3Jlc3RvcmVfYWxsIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfbDJjZyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2ludGxfdnBjX25hdCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Zjc19wYXkiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9sMmNnX2ludGwiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9hX2FwLXNvdXRoZWFzdC0xZSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FfcnUtbW9zY293LTFiIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYV9hcC1zb3V0aGVhc3QtMWQiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9hX2FwLXNvdXRoZWFzdC0xZiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX29wX2dhdGVkX21lc3NhZ2VvdmVyNWciLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3NfYzciLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3NfZ3B1X2FpMiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX21hcF92aXNpb24iLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3NfcmkiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9hX2FwLXNvdXRoZWFzdC0xYyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FfcnUtbm9ydGh3ZXN0LTJjIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfaWVmX3BsYXRpbnVtIiwiaWQiOiIwIn1dLCJwcm9qZWN0Ijp7ImRvbWFpbiI6eyJuYW1lIjoicWluZ3l1Z2UwMDYiLCJpZCI6IjA4OGIyZGRiNWYwMGYzODUwZjgyYzAwNzRiNzdjMDYwIn0sIm5hbWUiOiJjbi1ub3J0aC00IiwiaWQiOiIwOGM5MWI0ZjcyMDAxMDY3MmYwZmMwMDdhYmM2OWE0ZCJ9LCJpc3N1ZWRfYXQiOiIyMDIyLTAxLTI2VDA1OjA5OjU4LjIzNzAwMFoiLCJ1c2VyIjp7ImRvbWFpbiI6eyJuYW1lIjoicWluZ3l1Z2UwMDYiLCJpZCI6IjA4OGIyZGRiNWYwMGYzODUwZjgyYzAwNzRiNzdjMDYwIn0sIm5hbWUiOiJxaW5neXVnZTAwNiIsInBhc3N3b3JkX2V4cGlyZXNfYXQiOiIiLCJpZCI6IjA4OGIyZGRjNGMwMGYyZDAxZjAzYzAwN2FjYjE0YjVmIn19fTGCAcEwggG9AgEBMIGXMIGJMQswCQYDVQQGEwJDTjESMBAGA1UECAwJR3VhbmdEb25nMREwDwYDVQQHDAhTaGVuWmhlbjEuMCwGA1UECgwlSHVhd2VpIFNvZnR3YXJlIFRlY2hub2xvZ2llcyBDby4sIEx0ZDEOMAwGA1UECwwFQ2xvdWQxEzARBgNVBAMMCmNhLmlhbS5wa2kCCQDcsytdEGFqEDALBglghkgBZQMEAgEwDQYJKoZIhvcNAQEBBQAEggEAN+jehm7489IQoQav6PS5ktvWI4skSKE212mYTTgBHifWx+V5i0kAkliUlE8WFTufJ2Mas-XuNBugrqfDG61AnHML57g0d+EpnQm9ml-B7MtSRfjZZCtWkSMAtu+hIj6Y+juoJ14MMVgl-E2aj95UOH95uhkqahSbkVnGWS0IpDKojy8p8oo0slKPb8F4C+t+iG2u+8XnsK6pTRfgzjjlmN8izknoS2XfzocRVUMIUq3p0ExT5eVBY5fZ15hZZ8x4pBuakm29P3WB9+LHO5-lYeAOmkem+WrqtRgx3XX-7ywYb7l6ZwNNc7wq8iPkoxvRbT4UxZ8TKHWrx4tXOsLQqA=="
headers = {'Content-Type': 'application/json', 'X-Auth-Token': token}

f = open('../data/midu/extract.txt')
lines = f.readlines()
f.close()
#"categories": ['ad', 'politics', 'porn', 'abuse', 'contraband', 'flood'],
new_lines = []
messages = []
for line in lines:
	text = line
	data= {
	        "categories": ['porn'],
	        "items": [
	            {"text": text, "type": "content"}
	        ]
	        # items: 待检测的文本列表，目前暂时每次只支持传一个item。
	        # 待检测文本编码格式为“utf-8”，限定5000个字符以内，文本长度超过5000个字符时，只检测前5000个字符。
	    }

	response = requests.post(url, headers=headers, json=data, verify=False)
	#import ipdb;ipdb.set_trace()
	res = response.content.decode('unicode_escape')
	print(res)
	if "\"suggestion\":\"block\"" in res:
		new_lines.append(line)
		messages.append(res)

f = open('../data/midu/filted.txt', 'w')
f.writelines(new_lines)
f.close()

f = open('../data/midu/message.txt', 'w')
f.writelines(messages)
f.close()
