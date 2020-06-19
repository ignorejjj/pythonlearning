import requests
import re
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from urllib.request import urlopen
import os 
import os.path
import threadpool

header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45"}
pattern=re.compile('https.*?\.jpg')
opt = webdriver.ChromeOptions()
opt.set_headless()
driver=webdriver.Chrome(options=opt)   #设置无头模式    

list_zhihu=['https://www.zhihu.com/question/35931586',  # 身材好是一种怎样的体验？
            'https://www.zhihu.com/question/35931586',  # 你的日常搭配是什么样子？
            'https://www.zhihu.com/question/61235373',  # 女生腿好看胸平是一种什么体验？
            'https://www.zhihu.com/question/28481779',  # 腿长是一种什么体验？
            'https://www.zhihu.com/question/19671417',  # 拍照时怎样摆姿势好看？
            'https://www.zhihu.com/question/20196263',  # 女性胸部过大会有哪些困扰与不便？
            'https://www.zhihu.com/question/46458423']  # 短发女孩要怎么拍照才性感？
list_title=["身材好是一种怎样的体验？",
            "你的日常搭配是什么样子？",
            "女生腿好看胸平是一种什么体验？",
            "腿长是一种什么体验？",
            "拍照时怎样摆姿势好看？",
            "女性胸部过大会有哪些困扰与不便？",
            "短发女孩要怎么拍照才性感？"]
url=[]          #保存图片url

def menu():
    for i in range(1,8):
        print(str(i)+"."+list_title[i-1])
    print("请输入要下载的序号:",end='')
    number=input()
    number=int(number)-1       
    driver.get(list_zhihu[int(number)])
    print("请输入要下载的页面数:",end='')
    page=input()
    excute(int(page))
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    data=soup.find_all('noscript')
    for j in data:
        k=pattern.findall(str(j))
        url.append(k[0])
    download(number)
    print("下载完成!")


def excute(times):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/button").click()   #把弹出的登录框关掉
        for i in range(times):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[3]/a").click()  #显示更多内容按钮
                print("点击按钮成功")
                print("第"+str(i)+"页正常加载")
                time.sleep(1)
            except:
                print("第"+str(i)+"页正常加载")
    except:
        print('正常运行')
        for i in range(times):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[3]/a").click()  #显示更多内容按钮
                print("点击按钮成功")
                print("第"+str(i)+"页正常加载")
                time.sleep(1)
            except:
                print("第"+str(i)+"页正常加载")

def download(number):
    t=1
    flag=1
    for url_image in url:
        r=requests.get(url_image,headers=header)
        path='E:\learning\其它\p\summer learning\{0}'.format(list_title[int(number)])
        if not os.path.exists(path):
            os.mkdir(path)
            flag=0
        else:
            if(flag==1):
                print(path+"目录已存在!")
                flag=0
            else:
                flag=0
        open('E:\learning\其它\p\summer learning\{0}\{1}.jpg'.format(list_title[int(number)],str(t)), 'wb').write(r.content)
        print('第'+str(t)+"个照片下载成功")
        t=t+1

menu()
 


""" list_number=[0,1,2,3,4]          
pool=threadpool.ThreadPool(5)
reque = threadpool.makeRequests(menu_pool,list_number)
[pool.putRequest(req) for req in reque]
pool.wait() """     #无法完成多线程




    
