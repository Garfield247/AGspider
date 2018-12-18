# -*- coding: utf-8 -*-
# @Date    : 2018-12-17
# @Author  : LvGang/Garfield
# @Email   : Garfield_lv@163.com

import re
import os
import json
import requests
from urllib import parse

class AGSpider(object):
    """docstring for AGSpider"""
    def __init__(self):
        self.api = "http://www.cgris.net/query/o.php"
        self.headers = {
            'Accept':'text/javascript, text/html, application/xml, text/xml, */*',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'en-US,en;q=0.9',
            'Content-type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Host':'www.cgris.net',
            'Content-Length':'148',
            'Origin':'http://www.cgris.net',
            'Referer':'http://www.cgris.net/query/do.php',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest',
        }
        self.fp = open('./agdata.json','a',encoding='utf-8')





    def requests_hanlder(self,formdata):
        '''
        说明：构造POST请求，返回响应
        参数：formdata,Dict,POST请求的参数
        返回值：response，response Object ，响应
        '''
        response = requests.post(url=self.api,data=formdata,headers=self.headers)
        return response

    def parse_menu(self,response):
        '''
        说明：解析作物列表
        参数：response，response Object ，响应
        返回值：
        '''
        # print(eval(response.text))
        return json.loads(response.text)
        # pass

    def parse_query(self,response):
        '''
        说明：解析作物列表
        参数：response，response Object ，响应
        返回值：
        '''
        # print(re.findall(r'\["(.*?)"\]',response.text))
        return re.findall(r'\["(.*?)"\]',response.text)
        # pass

    def parse_item(self,response):
        '''
        说明：解析作物列表
        参数：response，response Object ，响应
        返回值：
        '''
        # print(json.loads(response.text))
        return json.loads(response.text)
        # pass

    def save_data(self,item):
        '''
        说明：数据存储
        参数：item ,Dict，数据
        返回值：
        '''
        data = json.dumps(item,ensure_ascii=False)
        self.fp.write(data+'\n')

    def crawl(self):
        '''
        说明：采集方法
        参数：无
        返回值：
        '''
        menu_fd = {'action':'menu','_':''}
        menu_res = self.requests_hanlder(menu_fd)
        for menu in self.parse_menu(menu_res):
            query_fd = {'action': 'query','p':'{}','croptype':[parse.quote(m) for m in menu],'_':'' }
            query_res = self.requests_hanlder(query_fd)
            for query in self.parse_query(query_res):
                item_fd = {'action':'item','p':query,'croptype':[parse.quote(m) for m in menu], '_':'' }
                item_res = self.requests_hanlder(item_fd)
                item = self.parse_item(item_res)
                print(menu)
                item['作物分类'] = menu[1]
                item['作物名称'] = menu[0]
                self.save_data(item)



    def main(self):
        '''
        说明：主函数启动函数
        参数：response，response Object ，响应
        返回值：
        '''
        self.crawl()
        pass


if __name__ == '__main__':
    ags = AGSpider()
    ags.main()

