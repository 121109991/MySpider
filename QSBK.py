import requests
from bs4 import BeautifulSoup
import re
authors = []
contents = []
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"
}
url = "https://www.qiushibaike.com/text/"
html = requests.get(url,headers=headers)
text = html.text
con = BeautifulSoup(text, 'html.parser')
con_list = con.find_all('div', class_="article")  # 找到文章列表
for i in con_list:
       #author = i.find('h2').string  # 获取作者名字
       #new_author = re.sub("[\n]","",author) # 去\n
       #authors.append(new_author)
       #orl = i.find("div",class_="articleGender").string # 获取年龄
       #stats = i.find('div', class_="stats")
       #number = stats.find("i", class_="number").string # 获取好笑程度
       content = i.find('div', class_='content').find('span').get_text() #
       new_content = re.sub("[\n]","",content)
       contents.append(new_content)
       #print(new_content)