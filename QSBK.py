import requests
from bs4 import BeautifulSoup
import re
import time

def download_page(url):
       headers = {
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36",
              "cookie": 'gr_user_id=e8c710a7-9679-45f3-b7c6-593de2db90d2; _qqq_uuid_="2|1:0|10:1587996424|10:_qqq_uuid_|56:Y2JlMDY3ZjQ4Njc4ZjUwYTFhOGMwYWUxMTJiNWVhOTI2YzFkYmRmNw==|8b52c43f50dea83b24217f8b2f55d3fe199ff6845592b0617cb847281565bb85"; _ga=GA1.2.1729012026.1587996424; _gid=GA1.2.767862927.1587996424; grwng_uid=f72e4130-5405-4825-a9b1-b2c843fa7a19; _xsrf=2|b4c99afd|a676c762239d2e18aab02eda6c4cfaf8|1588043342; BAIDU_SSP_lcr=https://www.baidu.com/link?url=WtJH55P6MfWF44X6qArFkaFkMlSvAHIJHC6kFrpWsgxIc0O9xHE6Iym2_9ztgRcs&wd=&eqid=e9751261000529f2000000065ea79e4c; ff2672c245bd193c6261e9ab2cd35865_gr_session_id=f116817e-9bae-4340-8d22-618b34a42a01; Hm_lvt_2670efbdd59c7e3ed3749b458cafaa37=1587996424,1588001288,1588043343; ff2672c245bd193c6261e9ab2cd35865_gr_session_id_f116817e-9bae-4340-8d22-618b34a42a01=true; __cur_art_index=8601; Hm_lpvt_2670efbdd59c7e3ed3749b458cafaa37=1588043508'}

       r = requests.get(url,headers=headers)
       return r.text
def get_content(html):
       output = '''作者:{} 年龄:{} 性别:{} \n内容:{}\n点赞:{} 评论:{}\n-----------\n'''
       soup = BeautifulSoup(html,'html.parser')
       con = soup.find("div",class_='col1 old-style-col1')
       cont_list = con.findAll("div",class_='article')
       k = 1
       for cont in cont_list:
              author = cont.find('h2').string # 获取作者
              new_author = re.sub('[\n]',"",author)
              author_cont = cont.find('div',class_='articleGender') # 获取作者年龄和性别
              if author_cont is not None:
                     class_list = author_cont['class']
                     if class_list[1] == 'manIcon':
                            gander = "男"
                     elif class_list[1] == 'womenIcon':
                            gander = "女"
                     else:
                            gander = ''
              age = author_cont.string # 年龄
              content = cont.find('div',class_='content').get_text() # 获取内容
              new_content = re.sub('[\n]','',content)
              stat = cont.find('div',class_='stats')
              number = stat.find('span').find('i').string # 获取点赞数
              comments = stat.find('a',class_='qiushi_comments').find('i').string # 评论数
              save_text(output.format(new_author,age,gander,new_content,number,comments))
              print(f'*****第{k}篇写入成功*****')
              k +=1
              time.sleep(2)
def save_text(*args): # *args:当传入的参数个数未知，且不需要知道参数名称时
       for i in args:
              with open('qiubai.txt','a',encoding='utf-8') as f:
                     f.write(i)


def main():
       for page in range(1,14):
              print(f"正在爬取第{page}页>>>>>>>")
              url = f"https://www.qiushibaike.com/text/page/{page}/"
              html = download_page(url)
              get_content(html)
              time.sleep(4)
       print('*****爬取完毕*****')



if __name__ == '__main__':
    main()
