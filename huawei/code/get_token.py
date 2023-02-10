# return the token for authentication
# reference: https://support.huaweicloud.com/api-iam/iam_30_0001.html
import requests
identity = '''
{
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "domain": {
                        "name": ""        
                    },
                    "name": "",           
                    "password": ""    
                }
            }
        },
        "scope": {
            "project": {
                "name": "cn-north-4"  
            }
        }
    }
}
'''
headers = {"Content-Type":'application/json;charset=utf8'}
url = 'https://iam.cn-north-4.myhuaweicloud.com/v3/auth/tokens'

r = requests.request('POST',url,data=identity)
print(r)
print('Token:', r.headers['X-Subject-Token'])
