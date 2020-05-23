import requests
from bs4 import BeautifulSoup
import re
import time

def Get_Html(url):
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36",

    }
    re = requests.get(url,headers=headers)
    html = re.text
    return html
def Get_content(html):
    output = '''标题:{} \n地址房型:{} \n房价:{}\n-----------\n'''
    soup = BeautifulSoup(html,'html.parser')
    con = soup.find('div',class_='content__article').find('div',class_='content__list')
    con_list = con.findAll('div',class_='content__list--item--main')
    for i in con_list:
        title = i.find('a').string
        new_title = re.sub('[\n\s]','',title) #获取标题
        # print("标题: ",new_title)
        # print("等待两秒钟----->\n",)
        time.sleep(1)
        address = i.find('p', class_='content__list--item--des').get_text() # 获取地址
        new_address = re.sub('[\n\s]','',address)
        # print("地址房型: ",new_address)
        time.sleep(1)
        price = i.find('span',class_='content__list--item-price').find('em').string
        # print('房价：',price)
        time.sleep(1)
        op = output.format(new_title,new_address,price)
        save_text(output.format(new_title,new_address,price))
        print(op)
    print("本页爬取完成,准备爬取下一页.....")



def save_text(*args):  # *args:当传入的参数个数未知，且不需要知道参数名称时
    for i in args:
        with open('LianJia.txt', 'a', encoding='utf-8') as f:
            f.write(i)


if __name__ == '__main__':
    for t in range(1,100):
        print(f"正在爬取第{t}页---------->")
        url = f"https://sz.lianjia.com/zufang/luohuqu/pg{t}/#contentList"
        html = Get_Html(url)
        time.sleep(5)
        Get_content(html)
    print("*****爬取完成******")