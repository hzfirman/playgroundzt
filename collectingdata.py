#-*- coding:utf-8 -*-
import  requests
import re
from bs4 import BeautifulSoup
import os
import time

host_name="https://www.sothebys.com"
for i in range(12,300):
    try:
        url="https://www.sothebys.com/zh/auctions/ecatalogue/lot.%s.html/2019/ceramics-and-jades-from-the-collection-of-sir-quo-wei-lee-hk0902"%i#browser.get(url)
        #time.sleep(1)
        #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        path="D:\\拍卖行\\苏富比\\"
        headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
        html=requests.get(url,headers=headers)
        print(html)
        bsobj = BeautifulSoup(html.content, 'html.parser')
        auction_name=bsobj.find_all("h5",{"class":"alt"})
        print(auction_name[0].text)
        dir_list=os.listdir(path)
        if auction_name[0].text not in os.listdir(path):
            path=path+auction_name[0].text
            os.mkdir(path)
        print('——————')
        lot_number=bsobj.find_all("div",{"class":"lotdetail-lotnumber hidden-phone"})
        print(lot_number[0].text)
        print('——————')
        lot_condition=bsobj.find_all("p",{"class":"condition-desc"})
        #link_href=bsobj.find_all("img",{"src":"/content/dam/stb/lots/HK0/HK0902/045HK0902_7CNQC_2.jpg.webrend.256.256.png"})
        ##link_list=bsobj.find_all("img")
        for link in lot_condition:
            if "class" in link.attrs:
                print(link.get_text())
                print('——————')
        lot_name_tag= bsobj.find_all("div", {"class": "lotdetail-guarantee"})
        lot_name_list=[]
        for link in set(lot_name_tag):
            if "class" in set(link.attrs):
                lot_name_list.append(link.get_text())
                print(link.get_text())
                print('————————')
        lot_name_list=list(set(lot_name_list))
        lot_image_tag=bsobj.find_all("img", {"src":re.compile("\/content\/dam\/stb\/lots\/HK0\/HK0902\/.*")})
        image_list=[]
        file_count=0
        for link in set(lot_image_tag):
            if "src" in link.attrs:
                item=link.attrs["src"].split(".")
                image_list.append(item[0]+"."+item[1])
        image_list=list(set(image_list))
        for link in image_list:
                link=host_name+link
                response = requests.get(link, headers=headers)
                file_name = lot_name_list[0].replace("\r","").replace("\n","") + str(file_count)
                with open(path + auction_name[0].text+"\\"+file_name + ".jpg", "wb")as f:
                    f.write(response.content)
                file_count+=1
        for i in set(image_list):
            print(i)

    except OSError as e:
        print(e)
 # 返回空值，中断程序，或者执行另一个方案
    # 程序继续。注意：如果你已经在上面异常捕捉那一段代码里返回或中断（break），
    # 那么就不需要使用else语句了，这段代码也不会执行