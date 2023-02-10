# Huawei moderation api
## usage
- run `main.py` to run content moderation
- One piece text each time (文本长度限制：20000字节（约等于6666个字符数）)
- access_token的有效期为30天，需要每30天进行更换  (run `get_token.py`, copy the output to the `token` variable in main.py)
- the result is in json format
  - 格式参考：https://cloud.baidu.com/doc/ANTIPORN/s/Nk3h6xbb2
- 本接口用默认策略进行审核，默认策略开启了以下能力：
百度官方违禁词库，文本色情，暴恐违禁，政治敏感，恶意推广（默认违规标签包含：联系方式、软文推广），低俗辱骂
如果默认策略不满足您的审核需求，您可以进入内容审核平台创建自定义规则创建符合需求的审核策略。
  
## reference
https://cloud.baidu.com/doc/ANTIPORN/index.html