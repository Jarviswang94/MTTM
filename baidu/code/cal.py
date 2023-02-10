# coding=utf-8

import sys
import json
import base64
import time

# 保证兼容python2以及python3
IS_PY3 = sys.version_info.major == 3
if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode
    from urllib.parse import quote_plus
else:
    import urllib2
    from urllib import quote_plus
    from urllib2 import urlopen
    from urllib2 import Request
    from urllib2 import URLError
    from urllib import urlencode

# 防止https证书校验不正确
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


TEXT_CENSOR = "https://aip.baidubce.com/rest/2.0/solution/v1/text_censor/v2/user_defined";

"""
    调用远程服务
"""
def request(url, data):
    req = Request(url, data.encode('utf-8'))
    has_error = False
    try:
        f = urlopen(req)
        result_str = f.read()
        if (IS_PY3):
            result_str = result_str.decode()
        return result_str
    except  URLError as err:
        print(err)


# 获取access token
TOKEN = '24.1c0dd6eeb59d12d154c6b03fcda480de.2592000.1645088939.282335-25529213'

# 拼接文本审核url
text_url = TEXT_CENSOR + "?access_token=" + TOKEN

f = open('../data/midu/extract_train.txt')

lines = f.readlines()
f.close()
new_lines = []
messages = []
for line in lines:
    text = line
    result = request(text_url, urlencode({'text': text}))
    print(result)
    if "\"conclusion\":\"不合规\"" in result:
        print(result)
        new_lines.append(line)
        messages.append(result)

f = open('../data/midu/filted.txt', 'w')
f.writelines(new_lines)
f.close()

f = open('../data/midu/message.txt', 'w')
f.writelines(messages)
f.close()



    
