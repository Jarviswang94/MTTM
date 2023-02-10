# Huawei moderation api
## requirements
```pip install requests```
## usage
- run `main.py` to run content moderation
- One piece text each time (utf-8 encoding, <5000 words)
- needs to re-issue token every 24 hours (run `get_token.py`, copy the output to the `token` variable in main.py)
- the result is in json format
  - e.g  {"result":{"detail":{"abuse":["我日你"],"contraband":["白粉"]},"suggestion":"block"}}
  

## reference
- https://support.huaweicloud.com/api-moderation/moderation_03_0018.html
- endpoint https://developer.huaweicloud.com/endpoint?Moderation (we use 华北-北京四)