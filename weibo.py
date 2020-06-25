import requests
import os
import re
import json
from lxml import etree
from urllib.parse import parse_qs
import random

proxies = ["222.85.28.130:52590","117.191.11.80:80","117.127.16.205:8080","118.24.128.46:1080"]
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36 Edg/83.0.478.54",
        "Cookie":"SINAGLOBAL=7457588740430.159.1592025843723; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFApzrYxGPo-BP6UR6G7k6y5JpX5KMhUgL.Foq0e0e0Sh5pS0M2dJLoI0YLxKqL1-eL1hnLxKBLB.2LB--LxKnLB--LBK.LxKqL1hnL1K2LxK.L1K.LB-2LxK-LBK-LBo.LxKML1-BLBK2t; UOR=,,login.sina.com.cn; wvr=6; wb_view_log_6333340177=1440*9601.5; ALF=1624530891; SSOLoginState=1592994893; SCF=AqdfYFfepJEAxuCJ_ex48BSespGlAdzeTnCdqKW-KPkVALy2dgLwNbVLA5f0oRwnadcJXCXmzINkEJucE90xnf0.; SUB=_2A25z91wdDeRhGeBN6FES9C7NzDuIHXVQhcrVrDV8PUNbmtAKLUL7kW9NRJbVV1vXKsbdgr4Fv4jwJ9lbQELZG7-s; SUHB=0y0ZX-uVY9aLWJ; Ugrow-G0=6fd5dedc9d0f894fec342d051b79679e; _s_tentry=login.sina.com.cn; Apache=8924742892784.963.1592994896153; ULV=1592994896226:3:3:2:8924742892784.963.1592994896153:1592739885698; TC-V5-G0=4de7df00d4dc12eb0897c97413797808; webim_unReadCount=%7B%22time%22%3A1592994908325%2C%22dm_pub_total%22%3A34%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A87%2C%22msgbox%22%3A0%7D; TC-Page-G0=1ae767ccb34a580ffdaaa3a58eb208b8|1592994907|1592994891"}
params={'ajwvr':6,
        'id':"4367970740108457",
        'from':"singleWeiBo",
        'root_comment_max_id':""
        }
pic_list=[]


def download():
    t=1
    flag=1
    for url_image in pic_list:
        if(url_image!=''):
                r=requests.get(url_image,headers=headers)
                path='E:\learning\其它\p\summer learning\{0}'.format("weibo")
                if not os.path.exists(path):
                        os.mkdir(path)
                        flag=0
                else:
                        if(flag==1):
                                print(path+"目录已存在!")
                                flag=0
                        else:
                                flag=0
                open('E:\learning\其它\p\summer learning\{0}\{1}.jpg'.format("weibo",t), 'wb').write(r.content)
                print('第'+str(t)+"个照片下载成功")
                t=t+1

for num in range(20):
        url='https://weibo.com/aj/v6/comment/big'
        resp=requests.get(url,headers=headers,params=params,proxies={"http": random.choices(proxies)[0]})
        resp=json.loads(resp.text)
        if resp['code'] == '100000':
                html = resp['data']['html']
                print(html)
                html = etree.HTML(html)
                max_id_json = html.xpath('//div[@node-type="comment_loading"]/@action-data')[0]
                max_id=parse_qs(max_id_json)['root_comment_max_id'][0]  
                params['root_comment_max_id']=max_id
                data = html.xpath('//div[@node-type="root_comment"]')
                for i in data:
                        #nick_name = i.xpath('.//div[@class="WB_text"]/a/text()')[0]
                        #wb_text = i.xpath('.//div[@class="WB_text"][1]/text()')
                        pic_url = i.xpath('.//li[@class="WB_pic S_bg2 bigcursor"]/img/@src')
                        pic_url = 'https:' + pic_url[0] if pic_url else ''   
                        pic_list.append(pic_url)   


download()