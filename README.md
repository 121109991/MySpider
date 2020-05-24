

#### <img src="https://github.com/Huang-YuHang/MySpider/blob/master/image/logo.jpg" width="150" height="150" alt="logo"/>记录自己在学习爬虫的点点滴滴<img src="https://github.com/Huang-YuHang/MySpider/blob/master/image/logo2.jpg" width="150" height="150" alt="logo2"/>

###### Auto: Little_blue_cat  

###### From: Shenzhen, Guangdong, China

###### WeChat: ki1293160648

#### 																 :boxing_glove:**About me**:boxing_glove:

###### 我是一名在深圳就读的大三学生，就读的专业是软件技术Python方向，热爱技术，喜欢专研。这里主要是记录我学习爬虫知识的代码项目以及我对爬虫相关知识的总结和在写爬虫代码当中遇到的问题，同时也欢迎大家互相交流知识。

#### :package:`项目专区 `(记录我写的每个爬虫项目用到的库和方法):artificial_satellite:

#####  Taobao.py:arrow_lower_right:

> ------
>
> - ###### 项目介绍:
>
> 能爬取某宝用户所指定的商品数据,由于有反扒机制,每当定位到搜索商品名都会弹出登录框(目前暂未破解),所以此项目需要手动扫码登录,我设置了等待时间需要使用者在规定时间内扫码成功,不然会爬取失败。
>
> ------
>
> - ###### 使用到的库:
>
> [Selenium]:它能够模拟用户的真实操作,如自动打开浏览器(支持IE,Chome,Firefox),点击,输入,滑动窗口滚动条等操作。它的框架底层使用的是JavaScript。,
> [time]: 它是用来设置等待时间的,写爬虫要合理使用time,爬取的速度太快容易被反扒机制发现反而太慢又会影响效率,所以要不断测试取中间值。!!!要记住获取别人数据的同时也不要破坏别人的服务器哦!!!
> [re]: 它是匹配字符串的模块，它的功能基于正则表达式实现的，这里我只讲下我用到的功能,其他详细的功能使用可到技术专区查看。
> [csv]: 我们爬取到数据需要存储起来,如果想存储到excel表格就会用到csv库
>
> ------
>
> - 实现过程:
>
>   首先我定义了四个函数,这里我要说一下我每个函数都的作用。
>
>   -  获取网页 ：def search_product(key)
>
>     ```python
>     driver.get(f"https://s.taobao.com/search?q={key}&imgfile=...)
>     wraper = driver.find_element_by_xpath('//div[@class="total"]').text
>     pages = re.findall('(\d+)',wraper)[0]
>     return pages
>     ##第二行我分析出每个不同商品的url只是q="商品名"不一样,其他的都是一样的。所以我从main函数传递进来一个用户输入的商品key,对url进行格式化就能输出用户想要的商品网页
>     
>     ##第二行代码是找到了网页中的最大页数,因为每个商品的最大页数可能不一,所以我要找到它的最大页数然后放进for循环次数里面就能有效的爬取不会做多余的操作.
>     
>     ##第三行是再找到最大页数中参杂了一些多余的字符串,而我只想要数字,我就用到了re模块里re.findall('(\d+)',wraper)表示\d+只是查找数字,返回的是一个列表
>     
>     ##最后return返回最大页数
>     ```
>
>   -  解析数据:：def get_product()
>
>     ```python
>     divs = driver.find_elements_by_xpath('//div[@class="items"]...)
>     for div in divs：
>         info = div.find_element_by_xpath('.//div[@class=",,,).text
>         pace = ...
>         dealcnt  = ...
>     
>     ##第一行这里使用Xpath方法找到所有详细商品所在div里。
>     //div这里的双斜杠表示查找所有的div
>     
>     ##第二行通过for循环遍历获取一个详细商品中的名称,价格,购买人数等等。
>     .//div这里双斜杠前加了个.表示选取当前节点下的div节点      
>     ```
>
>   -  保存数据：def save_csv(*args)
>
>     ```python
>     with open(f"{keyword}.csv",mode='a',newline='') as f
>             csvwrite = csv.writer(f,delimiter=',')
>             csvwrite.writerow(args)
>     #函数中的*args参数,表示的是可变位置参数,它是一个元组传入的参数会被放进元组里。
>     #mode='a表示文件写入方式,a是表示向文件追加数据
>     #newline=''表示新行添加,否则会一直写在同一行里
>     delimiter='，'是分隔符
>     ```
>
>   -  主函数：def main(): 
>
>     ```python
>     pages = search_product(keyword)
>     num = 0
>     for page in range(1,int(pages)+1):
>             driver.get(f"https://s.taobao.com/sear...8&s={num}")
>             num += 44
>             get_product()
>     
>     ##主函数主要是做翻页功能的设计,先获取search_product函数返回的最大页数的值放入for循环中,分析出每一页的尾椎都会相加44,所以每爬取完一样都会让num+44。
>     ```
>
>     :end:

------



#### :memo: `技术专区` (记录用过的方法,便于以后需要时候查询):artificial_satellite:

##### `获取数据大区`

##### `解析数据大区`

######         `正则表达式分区`

######         `Xpath分区`

######         `BeautifulSoup分区`

######         `Json分区`

##### `存储数据大区`

######         `CSV分区`

######         `Mysql分区`

#### :raising_hand_man:`疑点专区` (记录我写代码中碰到解决困难的问题):artificial_satellite:


