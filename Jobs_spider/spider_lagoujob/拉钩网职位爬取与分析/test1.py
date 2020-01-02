'''

'''
import json
import multiprocessing
import threading
import time
# import xlwt
import pandas as pd
from pandas import DataFrame, Series
import re
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gevent import monkey;monkey.patch_all()#导入猴子补
import gevent


chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver_win32\chromedriver'

# 关闭浏览器显示
chrome_options = Options()
# chrome_options.add_argument('--headless')


chrome_options.add_argument('--referer=http://www.baidu.com')
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument(
            'user-agent="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"')
chrome_options.add_argument("--proxy-server=http://127.0.0.1:9000")
driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=chrome_options)
driver.execute_script('Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});')
# driver.add_cookie({'domain': '.zhipin.com', 'name': '__zp_stoken__', 'value': '4f130jhu%2B1ie7Qc%2FyBzF3oFeYaVj0o47zA%2BeD4w9ONInFNrCmMYTYQECHK60LLufjYbHxkPK9fiObCNgllUPEP8B%2FVR5isB3W5X%2BCdpm1C2wtMBsHoM6sfdlLSGuyMS2a3Za'})
driver.get('https://www.zhipin.com/c101280600-p100109/?ka=search_100109')