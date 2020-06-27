import requests
from bs4 import BeautifulSoup
import re
import random
import random


class DYTT():
    def _init_(self,movie_name):
        self.params={"keyword":movie_name.encode('gb2312'),"typeid":1}        #传入参数
        self.proxies = ["58.18.133.101:56210"]
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36 Edg/83.0.478.54"}
        self.url="http://s.dydytt.net/plus/s0.php"
        self.pattern_movie_url=re.compile('\/html/.*?\.html')    #在搜索结果中匹配电影界面的url
        self.urls=[]        #保存电影界面链接
        self.name=[]
        self.num=0
        self.down_url=[]     #存放电影的下载链接
    
    def Search_movies(self):        
        #搜索电影，返回链接
        html=requests.get(self.url,params=self.params,headers=self.headers)#proxies={"http": random.choices(self.proxies)[0]})
        html.encoding='gb2312'              #避免乱码
        sp_search_data=BeautifulSoup(html.text,"html.parser")
        search_data=sp_search_data.find_all("b")                    
        #search_data下标从3到len(search_data)-3都是有用信息,search_data[i].text为电影名
        movie_urls=self.pattern_movie_url.findall(str(search_data))    
        #movie_url保存所有指向电影界面的url，对应下标为search_data的的下标-3
        for i in range(3,len(search_data)-3):
            self.urls.append(movie_urls[i-3])
            self.name.append(search_data[i].text)
            self.num=self.num+1
        return movie_urls
    
    def Excute_urls(self):
        #处理电影链接为完整的url
        url='https://www.ygdy8.com/'
        for i in range(len(self.urls)):
            self.urls[i]=url+self.urls[i]
        
    
    def analyse_url(self):
        #分析电影界面，提取下载链接及电影信息
        for url in self.urls:
            html=requests.get(url,headers=self.headers)
            html.encoding='gb2312'
            sp_data=BeautifulSoup(html.text,'html.parser')
            download_url=sp_data.find_all("td",{"style":"WORD-WRAP: break-word"})[0].find("a").text
            self.down_url.append(str(download_url))

        

            
        
if __name__=='__main__':
    movie=DYTT()
    print("请输入电影名:",end='')
    movie_name="初恋"
    movie._init_(movie_name)
    x=movie.Search_movies()
    movie.Excute_urls()
    movie.analyse_url()
    print(movie.down_url)
    











