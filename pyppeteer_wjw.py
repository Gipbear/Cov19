# -*- coding:utf-8 -*-
# author: Grizzly
# datetime:2020/11/17 22:34
# software: PyCharm
# source: https://blog.csdn.net/wenxuhonghe/article/details/106411570
# way: 使用pyppeteer爬取国家卫健委疫情数据

import asyncio
import re

from bs4 import BeautifulSoup
from pyppeteer import launch


# 将pyppeteer封装成fetch_url函数，发起网络请求，获取网页源码
async def pyppeteer_fetch_url(url):
    browser = await launch({'headless': False, 'dumpio': True, 'autoClose': True})  # 启动chromium
    page = await browser.newPage()  # 在浏览器上创建新页面并返回

    await page.goto(url)  # 前往url
    await asyncio.wait([page.waitForNavigation()])  # 等待页面导航
    str = await page.content()  # 返回页面中完整的html内容
    await browser.close()  # 关闭浏览器
    return str


# 按照url调用pyppeteer进行爬取
def fetch_url(url):
    return asyncio.get_event_loop().run_until_complete(pyppeteer_fetch_url(url))


# 获取爬取页面的url
def get_page_url():
    for page in range(1, 13):
        if page == 1:
            yield 'http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml'
        else:
            url = 'http://www.nhc.gov.cn/xcs/yqtb/list_gzbd_' + str(page) + '.shtml'
            yield url


# 获取页面中每天疫情报道的url
def get_title_url(main_html):
    bs_obj = BeautifulSoup(main_html, 'html.parser')  # 使用html.parser解析器解析页面
    title_list = bs_obj.find('div', attrs={"class": "list"}).ul.find_all("li")  # 按照路径找到所有有关url的li标签
    # 补全完整的页面url
    for item in title_list:
        full_link = "http://www.nhc.gov.cn" + item.a["href"]  # a标签下的href属性（url链接）
        page_title = item.a["title"]  # a标签下的title属性（标题）
        page_date = item.span.text  # span标签下的文本内容（时间）
        yield page_title, full_link, page_date


# 获取页面有关内容
def get_content(page_html):
    bs_obj = BeautifulSoup(page_html, 'html.parser')
    cnt = bs_obj.find('div', attrs={"id": "xw_box"}).find_all("p")  # 按照路径找到所有关于文本的p标签
    page_content = ""
    if cnt:
        for item in cnt:
            page_content += item.text
        return page_content
    return "爬取失败！"


def re_content(content):
    pattern = "确诊病例(\d+).*?死亡病例(\d*).*?疑似病例(\d*).*?出院病例(\d*).*?密切接触者(\d*)"
    result_data = re.search(pattern,content)
    return result_data.groups()


if "__main__" == __name__:
    for main_url in get_page_url():
        s = fetch_url(main_url)  # 主页获得所有子页的html页面
        for title, link, date in get_title_url(s):
            print(title, link)
            # 如果日期在1月21日之前，则直接退出
            mon = int(date.split("-")[1])
            day = int(date.split("-")[2])
            if mon <= 1 and day < 21:
                break
            html = fetch_url(link)  # 子页获取html页面
            content = get_content(html)  # 获取html页面中的字符串内容
            print(content)
            data = re_content(content)
            print(data)
            print("-----" * 20)