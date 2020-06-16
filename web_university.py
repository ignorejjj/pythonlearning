import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt




def getonepage(year):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.4'}
    url='http://www.zuihaodaxue.com/zuihaodaxuepaiming-zongbang-'+str(year)+'.html'
    response=requests.get(url,headers=headers)
    return response.content

def parse_onepage(html,year):       #实际上pandas可以直接解析url链接
    tables=pd.read_html(html)[0]    #tables这个列表仅有一个元素
    tb1=tables.drop(['学校类型','总分'],axis=1)  #axis参数为0代表删除行，为1代表删除列    
    tb2=tb1.drop(tb1.index[100:778])
    #tb2.to_excel('1.xlsx')  保存到excel中
    data=tb2.groupby(['省市'])   #按省市分组
    list_area=[]
    list_num=[]
    for i in data:
        list_area.append(i[0])
    for i in data:
        list_num.append(len(i[1]))
    plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
    plt.pie(list_num,labels=list_area,autopct="%3.1f%%")
    plt.show()
html=getonepage(2020)
parse_onepage(html,2020)
