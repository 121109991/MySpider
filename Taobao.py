import time
from selenium import webdriver
import csv
import re
def search_product(key):
    driver.get(f"https://s.taobao.com/search?q={key}&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200513&ie=utf8&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=0")
    driver.maximize_window()
    print("扫描二维码登录")
    time.sleep(7.5)
    print("请稍等.....正在解析最大页数")
    time.sleep(2)
    wraper = driver.find_element_by_xpath('//div[@class="total"]').text #最大页数
    pages = re.findall('(\d+)',wraper)[0] # 解析页数数字
    print(f"最大页数是: {pages}")

    return pages
def get_product():
    time.sleep(2)
    i = 1
    divs = driver.find_elements_by_xpath('//div[@class="items"]/div[@data-category="auctions"]')
    for div in divs:
        info = div.find_element_by_xpath('.//div[@class="row row-2 title"]/a').text #产品名称
        time.sleep(0.8)
        pirce = div.find_element_by_xpath('.//div[@class="price g_price g_price-highlight"]/strong').text #产品价格
        dealcnt = div.find_element_by_xpath('.//div[@class="deal-cnt"]').text #购买人数
        shop = div.find_element_by_xpath('.//div[@class="row row-3 g-clearfix"]/div[@class="shop"]/a/span[2]').text #商家名称
        time.sleep(1.5)
        location = div.find_element_by_xpath('.//div[@class="row row-3 g-clearfix"]/div[@class="location"]').text #商家地址
        print(f'''{mark}\n商品名称:{info}\n{mark}\n商家名称:{shop} 商品价格:{pirce} \n购买人数:{dealcnt} 商家地址:{location}\n''')
        i +=1
        save_csv(info,pirce,dealcnt,shop,location)
    time.sleep(3)

def save_csv(*args):
    with open(f"{keyword}.csv",mode='a',newline='') as f :#newline新行添加
        csvwrite = csv.writer(f,delimiter=',')
        csvwrite.writerow(args)
def main():
    pages = search_product(keyword)
    num = 0
    for page in range(1,int(pages)+1):
        print(f"{mark2}正在爬取第{page}页{mark2}")
        driver.get(f"https://s.taobao.com/search?q={keyword}&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200513&ie=utf8&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s={num}")
        num += 44
        get_product()

if __name__ == '__main__':
    mark = "-" * 100  # 打印分割符号
    mark2 = "*"*25
    driver = webdriver.Chrome()
    keyword = input("输入你要搜索的商品名: ")
    main()


