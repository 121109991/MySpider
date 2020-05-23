import csv
import os
import requests
from bs4 import BeautifulSoup
import re
import time


def spider(headers):
    pass

def Pare_data():
    kong = " "
    http = "http:"
    con_list = soup.find("div", class_="content")
    title_list = con_list.findAll("h2")
    i = 1
    k = 0
    for tl in title_list:
        title = tl.text
        print("****************************" + title + "************************************")
        save_csv(title)
        tuku_list = con_list.findAll("div", class_="y-tuku235")
        for tuku in tuku_list[k:i]:
            li_list = tuku.findAll("li")
            for li in li_list:
                title_list = li.findAll("p", class_="title")
                for title in title_list:
                    a1 = title.find("a").text
                    a = "车型: " + title.find("a").text
                    print("车型:", a)  # 车型
                    price_list = li.findAll("p", class_="price")
                    for price in price_list:
                        b = "指导价区间: " + price.find("em").string
                        # print("  价格:",b)
                        save_csv(a, b)
                        img_list = li.findAll("div", class_="img")
                        for img in img_list:
                            c = img.find("img").get("src")
                            # print("图片: ",c) #图片
                            img_url = requests.get(c)
                            im = img_url.content
                            path = f'E:\\My Spider\\{h1}\\'
                            if not os.path.exists(path):
                                os.mkdir(path)
                            with open(f'{path}{a1}.jpg', 'wb') as f:
                                f.write(im)
                            time.sleep(2)
                            d = http + img.find("a").get("href")  # 获取车系首页url
                            # print("车系首页: ",d,"\n")
                            html = requests.get(url=d, headers=headers).text
                            new_soup = BeautifulSoup(html, "html.parser")
                            try:
                                thead_list = new_soup.find("table").findAll("thead")
                                j = 0
                                m = 1
                                for thead in thead_list:
                                    tr_list = thead.findAll("th")
                                    # for tr in tr_list:
                                    th1 = tr_list[0].text
                                    th3 = tr_list[2].text
                                    th4 = tr_list[3].text
                                    th5 = tr_list[4].text
                                    # print(th1,"                         ",th3,"            ",th4,"       ",th5,"\n")
                                    save_csv(th1, th3, th4, th5)

                                    tbody_list = new_soup.find("table").findAll("tbody")
                                    for tbody in tbody_list[j:m]:
                                        tr_list = tbody.findAll("tr")
                                        for tr in tr_list[0:20]:
                                            span = tr.find("span").text
                                            print(span)
                                            td = tr.findAll("td")[2].text
                                            # print(td,end="    ")
                                            td2 = tr.findAll("td")[3]
                                            td3 = td2.find("span").text
                                            new_td2 = re.findall('(\d+)', td3)
                                            zhidao = new_td2[0] + "." + new_td2[1] + "万"
                                            # print("  ",new_td2[0]+"."+new_td2[1]+"万",end="         ")
                                            td4 = tr.findAll("td")[4]
                                            new_td4 = td4.find("span").text
                                            # print(new_td4)
                                            save_csv(span, td, zhidao, new_td4)
                                            time.sleep(1.5)
                                        save_csv(kong)
                                    j += 1
                                    m += 1
                                print("\n", "**********************************************************")
                                time.sleep(3)
                            except:
                                try:
                                    title = new_soup.find("div", class_="type_title")  # 车型标题
                                    span_list = title.findAll("span")
                                    hun1 = span_list[0].text  # 插电式混动
                                    hun2 = span_list[1].text  # 指导价
                                    hun3 = span_list[2].text  # 补贴后参考价
                                    save_csv(hun1, hun2, hun3)
                                    li_list = new_soup.find('ul', class_="listul clearfix").findAll("li",
                                                                                                    class_="listli")  # 车型具体标题
                                    for li in li_list:
                                        span2 = li.findAll("span")
                                        huncar1 = span2[0].text  # 混动车型
                                        huncar2 = span2[1].text  # 混动指导价
                                        huncar3 = span2[2].text  # 混动补贴后参考价
                                        print(huncar1)
                                        save_csv(huncar1, huncar2, huncar3)
                                    save_csv(kong)
                                    time.sleep(1.5)
                                    print("\n", "**********************************************************")
                                    time.sleep(3)
                                except:
                                    pass
                                continue
                            continue
        i += 1
        k += 1
    print("*******************************爬取完成************************************")


def save_csv(*args):
    with open(f"{path}{h1}.csv", mode='a', newline='') as f:
        csvwrite = csv.writer(f, delimiter=',')
        csvwrite.writerow(args)


def main():
    Pare_data()


if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36",
        "Referer": "http://db.auto.sina.com.cn/price-34-2.html",
        "Upgrade-Insecure-Requests": "1",
    }
    for u in range(1,300):
        url = f"http://db.auto.sina.com.cn/b{u}.html"
        res = requests.get(url, headers).text
        soup = BeautifulSoup(res, "html.parser")
        h1 = soup.find("h1").text
        path = f'E:\\My Spider\\{h1}\\'
        if not os.path.exists(path):
            os.mkdir(path)
        main()
