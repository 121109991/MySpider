'''
Author:Litle_blue_cat
Time:2020/08/19
version: 1.0.0.0
'''
import os
import time
import requests
from bs4 import BeautifulSoup
import re
from fake_useragent import UserAgent
import random

def get_html(url): #获取首页数据
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    re = requests.get(url,headers=headers)
    html = re.text
    return html

def get_ProductUrl(html): #解析首页数据,提取分类url地址
    # print("获取首页数据成功,开始解析首页数据")
    dic = dict()
    soup = BeautifulSoup(html,'html.parser')
    con_List = soup.find('ul', class_='drawer-guide').findAll('li')
    for i in con_List:
        try:
            title = i.find('a').string
            a = i.find('a').get('href')
            if a == 'javascript:;':
                a = 'None'
            # print(title+a)
            title_dic = {f'{title}': f'{a}'}
            dic.update(title_dic)
        except:
            break
    del dic['Home']
    del dic['Jewelry Beads']
    del dic['Jewelry Findings']
    del dic['Beading Supplies']
    del dic['Stringing Materials']
    del dic['Jewelry & Watches']
    del dic['Hair Accessories & Findings']
    del dic['Sewing & DIY Crafts']
    url_dict = dict()
    for t, y in zip(list(dic.values())[7:8], list(dic.keys())[7:8]): #大分类
        url_dict.clear()
        path = f'E:\\My Spider\\PandawholeSpider\\{y}\\'
        if not os.path.exists(path):
            os.mkdir(path)
        print('现在的大分类区域是:'+y)
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        re = requests.get(url=t,headers=headers).text
        soup = BeautifulSoup(re, 'html.parser')
        # time.sleep(2)
        try:
            li_list = soup.find('ul', class_='CategoryProList').findAll('li')
            for li in li_list: #小分类
                title = li.find('a').get('title')
                href = li.find('a').get('href')
                # print(title + ' ' + href)
                # time.sleep(random.randint(1,2))
                href_dict = {f'{title}': f'{href}'}
                url_dict.update(href_dict)
                # print(url_dict)
            One_commodityUrl(url_dict,path)
            print('-' * 40 + '小分类区域爬取完成' + '-' * 40)
            # print(url_dict)
            # time.sleep(random.randint(2,4))
        except:
            new_href_dict = {f'{y}': f'{t}'}
            url_dict.update(new_href_dict)
            One_commodityUrl(url_dict,path)
            print('-'*40+'小分类区域爬取完成'+'-'*40)
            # time.sleep(random.randint(2, 4))
        # time.sleep(50)
        continue

def One_commodityUrl(url_dict,path):#获取单件商品Url地址
    # print('首页数据提取成功,开始获取单件商品数据')
    text_path = path
    One_commodity_dict = dict() #设置单件商品名和单件商品url地址的字典
    for value,title in zip(list(url_dict.values())[8:],list(url_dict.keys())[8:]):
        One_commodity_dict.clear()
        print('*'*40+f'正在爬取{title}小类的商品'+'*'*40)
        # print(value)
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        html = requests.get(url=value,headers=headers).text
        soup = BeautifulSoup(html,'html.parser')
        # time.sleep(2)
        con_list = soup.find('ul',class_="ProductShow").findAll("li") #找到商品列表
        for con in con_list: #小分类下的单件商品
            con_url = con.find('div',class_='ProImg').find('a').get('href') # 单件商品url地址
            # time.sleep(random.randint(1,3))
            con_title = con.find('div', class_='ProImg').find('img',class_="lazyload").get('alt') #单件商品名称
            # time.sleep(1)
            commodity_dict = {f'{con_title}':f'{con_url}'} #编写字典格式
            One_commodity_dict.update(commodity_dict) #写入字典
            # print(commodity_dict)
        get_content(One_commodity_dict,text_path,title)#return返回单件商品的url地址
    # # time.sleep(random.randint(2, 6))

def get_content(dict,text_path,title): #获取单件商品详细内容
    # print('单件商品数据成功,开始解析单个商品数据')
    i = 0
    for url in list(dict.values()):
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        try:
            html = requests.get(url=url,headers=headers).text
            shop_title = list(dict.keys())[i]
            print('-'*40+f'第{i+1}个商品'+'-'*40)
            output = '-'*40 + f'第{i+1}个商品' + '-'*40 +'\n'
            save_text(text_path, title, output)
            # print(shop_title)
            # print(url)
            soup = BeautifulSoup(html,'html.parser')
            # time.sleep(2)
            get_content_img(soup,text_path)
            url_list = get_Size_Options(soup)
            # print(url_list)
            for Size_Options_url in url_list:
                new_html = requests.get(url=Size_Options_url,headers=headers).text
                new_soup = BeautifulSoup(new_html, 'html.parser')
                # time.sleep(2)
                ul_list = new_soup.find('div',class_="DetailWrap").find('ul',class_="DetailText")
                Size_Options = 'Size Options:' + ul_list.find('li',class_='Coloroption').find('span').string #Size
                # time.sleep(random.randint(1, 3))
                Size = ul_list.find('li',class_='ProSize').find('strong').string # Size
                Weight =ul_list.find('li',class_='ProInf').findAll('p')[0].text #Weight
                # time.sleep(random.randint(1, 3))
                MOQ = ul_list.find('li', class_='ProInf').findAll('p')[1].text # MOQ
                Ready_time = ul_list.find('li', class_='ProInf').findAll('p')[2].text # ReadyTime
                # time.sleep(random.randint(1,3))
                Package_Szie = ul_list.find('li', class_='ProInf2').find('p').text # Package_Size
                output = f'{shop_title}''\n' \
                         f'{Size_Options}''\n' \
                         f'{Size}''\n' \
                         f'{Weight}'"        "f'{MOQ}'"        "f'{Ready_time}''\n' \
                         f'{Package_Szie}''\n'\

                # print(output)
                # print(Size_Options)
                # print(Size)
                # print(Weight+"        "+MOQ+"        "+Ready_time)
                # print(Package_Szie)
                save_text(text_path,title,output)
                get_content_table(ul_list,text_path,title)
            print(f"第{i+1}件商品爬取完毕")
            i += 1
        except:
            print(f"第{i + 1}件商品网页打不开,即将跳过")
        continue
    # time.sleep(random.randint(1, 3))

def get_Size_Options(soup):
    url_list = []
    ul_list = soup.find('ul', class_="Color_Options").findAll('li')
    for li in ul_list:
        url = li.find('a').get('href')
        url_list.append(url)
    return url_list

def get_content_table(ul_list,text_path,title): #获取单件商品表格内容
        try:
            Qty_table = ul_list.find('li', class_='QtyTable').find('ul').findAll('li')
            # min_Package = 'Package Qty:' + Qty_table[0].findAll('dd')[0].string # 最小购买量
            # Max_Parkage  ='Package Qty:' + Qty_table[0].findAll('dd')[1].string # 最大购买量
            min_Package = Qty_table[0].findAll('dd')[0].string  # 最小购买量
            # time.sleep(random.randint(1, 2))
            Max_Parkage = Qty_table[0].findAll('dd')[1].string  # 最大购买量

            # min_Priced = 'Priced per Package:' + re.sub('[\n\s]','',Qty_table[1].findAll('dd')[0].find('div').find('span').string)  # 最小单件购买价格
            # Max_Priced = 'Priced per Package:' + re.sub('[\n\s]','',Qty_table[1].findAll('dd')[1].find('div').find('span').string)  # 最大单件购买价格
            min_Priced =re.sub('[\n\s]','',Qty_table[1].findAll('dd')[0].find('div').find('span',class_="NewPrice").string)  # 最小单件购买价格
            # time.sleep(random.randint(1, 2))
            Max_Priced =re.sub('[\n\s]','',Qty_table[1].findAll('dd')[1].find('div').find('span').string)  # 最大单件购买价格

            # min_Pricing = 'Pricing Calculation:' + Qty_table[2].findAll('dd')[0].find('div').find('span').string  # 最小购买数量总价格
            # Max_Pricing = 'Pricing Calculation:' + Qty_table[2].findAll('dd')[1].find('div').find('span').string  # 最大购买数量总价格
            min_Pricing =Qty_table[2].findAll('dd')[0].find('div').find('span').string  # 最小购买数量总价格
            # time.sleep(random.randint(1, 2))
            Max_Pricing =Qty_table[2].findAll('dd')[1].find('div').find('span').string  # 最大购买数量总价格

            # print(min_Package,min_Priced,min_Pricing)
            # print(Max_Parkage,Max_Priced,Max_Pricing)
            output = 'Package Qty                   Priced per Package                   Pricing Calculation\n' \
                     f'{min_Package}''                            'f'{min_Priced}''                                    'f'{min_Pricing}\n' \
                     f'{Max_Parkage}''                            'f'{Max_Priced}''                                    'f'{Max_Pricing}''\n' \
                     '------------------------------------------------------------------------------------------''\n'
            # print(output)
            save_text(text_path, title, output)
            # print('Package Qty                   Priced per Package                   Pricing Calculation')
            # print(min_Package+'                      '+min_Priced+'             '+'                 '+min_Pricing)
            # print(Max_Parkage+'                         '+Max_Priced+'             '+'                 '+Max_Pricing)
        except:
            min_Priced = re.sub('[\n\s]', '',Qty_table[1].findAll('dd')[0].find('div').find('span', class_="NewPrice").string)# 最小单件购买价格
            min_Pricing = Qty_table[2].findAll('dd')[0].find('div').find('span').string  # 最小购买数量总价格
            output = 'Package Qty                   Priced per Package                   Pricing Calculation\n' \
                     f'{min_Package}''                            'f'{min_Priced}''                                    'f'{min_Pricing}''\n'\
                     '------------------------------------------------------------------------------------------''\n'
            # print(output)
            save_text(text_path,title,output)
            # print('Package Qty                   Priced per Package                   Pricing Calculation')
            # print(min_Package+'                      '+min_Priced + '             '+'                 '+min_Pricing)

def get_content_img(soup,text_path): #获取单件商品url地址
    img = 'https:'+soup.find('div',class_="DetailWrap").find('div',class_='ViewImg').find('img').get('src')
    img_name = img.split('/')[-1]
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    r = requests.get(img,headers=headers)
    with open(f'{text_path}'+'\\'f'{img_name}.jpg','wb') as f:
        f.write(r.content)
        f.close()

def save_text(text_path,title,output):  # *args:当传入的参数个数未知，且不需要知道参数名称时
        with open(f'{text_path}'+'\\'f'{title}.txt', 'a', encoding='utf-8') as f:
            f.write(output)

if __name__ == '__main__':
    url = "https://www.pandawhole.com/"
    html = get_html(url)
    get_ProductUrl(html)
