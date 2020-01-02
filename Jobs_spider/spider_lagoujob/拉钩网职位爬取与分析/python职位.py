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


def opendriver(city, filename):
    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver_win32\chromedriver'

    # 关闭浏览器显示
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=chrome_options)

    # 开启浏览器显示
    # driver = webdriver.Chrome(executable_path=chrome_path)

    # 深圳
    if city == '深圳':
        driver.get('https://www.lagou.com/shenzhen')
    elif city == '广州':
        driver.get('https://www.lagou.com/guangzhou')
    elif city == '北京':
        driver.get('https://www.lagou.com/beijing')
    elif city == '上海':
        driver.get('https://www.lagou.com/shanghai')
    elif city == '全国':
        driver.get('https://www.lagou.com/')
        time.sleep(1)
        btn1 = driver.find_elements_by_xpath('//div[@id="changeCityBox"]//a')[0]
        btn1.click()
    else:
        driver.get('https://www.lagou.com/')
        time.sleep(1)
        btn1 = driver.find_elements_by_xpath('//div[@id="changeCityBox"]//a')[0]
        btn1.click()
    input = driver.find_element_by_id('search_input')
    input.send_keys(filename)
    btn = driver.find_element_by_id('search_button')
    btn.click()
    time.sleep(1)
    return driver


def searchrun(infopaths, df, filename, driver, city):

    for infopath in infopaths:
        url = infopath.get_attribute('href')
        driver.execute_script('window.open("%s")' % url)
        driver.switch_to.window(driver.window_handles[1])
        name = driver.find_element_by_class_name('name').text
        company = driver.find_element_by_class_name('company').text
        salary = driver.find_elements_by_xpath('//dd[@class="job_request"]/h3//span')[0].text
        place = driver.find_elements_by_xpath('//dd[@class="job_request"]/h3//span')[1].text
        exp = driver.find_elements_by_xpath('//dd[@class="job_request"]/h3//span')[2].text
        school = driver.find_elements_by_xpath('//dd[@class="job_request"]/h3//span')[3].text
        type = driver.find_elements_by_xpath('//dd[@class="job_request"]/h3//span')[4].text
        dict1 = dict(
            name=name,
            company=company,
            salary=salary,
            place=place,
            exp=exp,
            school=school,
            type=type,
        )

        s = Series(dict1)
        df = df.append(s, ignore_index=True)

        driver.close()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
    print(df)
    df.to_csv('./%s/%s(%s).csv' % (filename, filename, city), mode='a')



# 协程, 关键字的各个城市分开执行
def fun2(filename, city):
    city = city.strip()
    print(city)
    driver = opendriver(city, filename)
    df = DataFrame()

    hides = driver.find_elements_by_xpath('//div[@class="pager_container"]//span[@page]')
    print(hides[-1].text)
    pages = int(hides[-1].text)
    for page in range(1, pages + 1):
        while True:
            try:

                # 页数步进
                if 2 * (page // 2) < (pages // 2):
                    pages_list = [i for i in range(0, page, 2) if (i != 0)] + [int(page)]
                    pages_list = list(set(pages_list))
                    pages_list.sort()
                else:
                    pages_list = [i for i in range(pages, page, -2) if (i != 0)] + [int(page)]
                    pages_list = list(set(pages_list))
                    pages_list.sort(reverse=True)

                print(pages_list)
                for pag in pages_list:
                    search = '//div[@class="pager_container"]//span[@page="%s"]' % (str(pag))
                    hide = driver.find_element_by_xpath(search)
                    print(hide.text)
                    driver.execute_script("arguments[0].click();", hide)
                    time.sleep(1)
                infopaths = driver.find_elements_by_xpath('//a[@class="position_link"]')

                searchrun(infopaths, df, filename, driver, city)
                print('保存成功，进入下一页')
                break
            except:
                print('出错，再一次开启这一页%s %s %s' % (filename, city, page))
                driver.switch_to.window(driver.window_handles[0])

                driver.quit()
                time.sleep(5)
                driver = opendriver(city, filename)

        driver.quit()
        time.sleep(5)
        driver = opendriver(city, filename)
    driver.quit()


# 线程，各个关键字分开执行
def func(filename, cityname):

    gList = []
    for city in cityname:
        g = gevent.spawn(fun2, filename, city)
        gList.append(g)
    gevent.joinall(gList)



if __name__ == '__main__':

    # 输入查询的信息
    time.sleep(1)
    filenames = input('请输入要搜索的关键字：')
    cityname = input('请输入范围(北上广深，全国,逗号隔开)：')
    cityname = re.split(r'[,;，]', cityname)
    filenames = re.split(r'[,;，]', filenames)
    print(cityname)
    print(filenames)


    # 后台设定查询的信息
    # filenames = ['web后端python', 'Unity', '软件工程师']
    # cityname = ['深圳', '北京', '上海', '广州', '全国']

    # filenames = ['web后端python']
    # cityname = ['深圳']

    for filename in filenames:

        if not os.path.exists('./' + filename):
            os.mkdir(filename)

        tList = []

        # 线程、进程切换
        # t = multiprocessing.Process(target=func, args=(filename, cityname))
        t = threading.Thread(target=func, args=(filename, cityname))
        tList.append(t)

        for x in tList:
            x.start()
        # for x in tList:
        #     x.join()