TARGET_URL = 'https://static.zhipin.com'
TARGET_URL1 = 'https://www.gstatic.com/'
TARGET_URL2 = 'https://t.zhipin.com/'
TARGET_URL3 = 'https://img'
TARGET_URL4 = ' https://cf'
INJECT_TEXT = 'Object.defineProperties(navigator,{webdriver:{get:() => false}});' #js执行文件


def response(flow):
    list1 = [TARGET_URL, TARGET_URL1, TARGET_URL2, TARGET_URL3]
    # list1 = [TARGET_URL, TARGET_URL1, TARGET_URL2]
    for TARGET_URL_ in list1:
        if flow.request.url.startswith(TARGET_URL_):
            return
    flow.response.text = INJECT_TEXT + flow.response.text

# mitmdump -s HTTPProxy.py -p 9000