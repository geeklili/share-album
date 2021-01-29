import requests
from lxml import etree


def get_one_page():
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
               "Accept-Encoding": "gzip, deflate, br",
               "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
               "Connection": "keep-alive",
               "Host": "www.meiriyiwen.com",
               "Upgrade-Insecure-Requests": "1",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36", }

    ret = requests.get('https://meiriyiwen.com/random', headers=headers)
    selector = etree.HTML(ret.text)
    title = selector.xpath('//*[@id="article_show"]/h1/text()')[0]
    author = selector.xpath('//*[@id="article_show"]/p/span/text()')[0]
    content_li = selector.xpath('//*[@id="article_show"]/div[1]/p/text()')
    return title, author, content_li
