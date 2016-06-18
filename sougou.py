#-*- coding: utf-8 -*-
import re
import requests
import time

class Spider(object):
    def __init__(self):
        print('开始爬虫....')

#get_source获取当前网页的源代码
    def get_source(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
                     }
        html = requests.get(url, headers)
        return html.text

#change_page实现翻页的功能，并保存所有url
    def change_page(self, url, total_page):
        now_page = int(re.search('page=(\d+)', url, re.S).group(1))
        page_group = []
        for i in range(now_page, total_page+1):
            link = re.sub('page=(\d+)', 'page=%d'%i, url, re.S)
            page_group.append(link)
        return page_group

    def get_urls_each_page(self, source):
        urls_each_page = re.findall('<a href="(.*?)" target', source, re.S)
        return urls_each_page

if __name__ == '__main__':
    all_urls = []
    url = 'http://weixin.sogou.com/weixin?query=北京&type=2&page=1&ie=utf8'
    fsh = Spider()
    all_links = fsh.change_page(url, 5)

    for link in all_links:
        print('deal with '+link)
        #time.sleep(10)
        html = fsh.get_source(link)
        #print(html)
        urls = fsh.get_urls_each_page(html)
        urls = urls[2:12]
        all_urls.append(urls)
    for l in all_urls:
        for u in l:
            print(u)









