import requests
import urllib
from bs4 import BeautifulSoup
import re
import os

file_count=0
next_link = "thread-1753221-636-1.html"
file_name_list=[]
path="D:\\python\\test\\补充部分\\"

def Schedule(a, b, c):
    '''
    a:已经下载的数据块
    b:数据库块的大小
    c:远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
        print('完成！')
    print('%.2f%%' % per)
def get_div(bsobj,file_count,file_name_list):#找到每个段落
    image_link=[]
    div_list=bsobj.find_all("div",{"class","pcb"})
    for div in div_list:
        name_tag=div.find_all("font",{"size":re.compile("4|5|6")})
        if len(name_tag)>0:
            file_count=0
            str1=name_tag[0].get_text()#得到标签的文本
            name="".join(str1.split())#去掉当中\xa0z这种空格
            file_name_list.append(name)
        image_link_list=div.find_all("img",{"file":re.compile("https://")})
        for i in image_link_list:
            file_name=file_name_list[-1]+str(file_count)
            link=i.attrs["file"]
            image_link.append(link)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
            response = requests.get(link, headers=headers)
            f = open(path + file_name + ".jpg", "wb")
            f.write(response.content)
            f.close()
            file_count+=1

def turn_to_page(file_count,next_link,file_name_list):#从起始页开始翻页
    while next_link is not None:
        url = "https://bbs.artron.net/" + next_link
        response = requests.get(url)
        bsobj = BeautifulSoup(response.text, 'html.parser')
        #print(bsobj)
        print("正在打印%s页的图片链接" % next_link)
        get_div(bsobj,file_count,file_name_list)
        next_page = bsobj.find("a", {"class": "nxt"})  # 获取下一页的链接
        if "href" in next_page.attrs:#假如有下一页，就获取链接
            next_link = next_page.attrs["href"]#得到下一页的网址
            if next_link != "thread-1753221-695-1.html":
                continue
            else:
                print("补充部分已结束")
            break
turn_to_page(file_count,next_link,file_name_list)