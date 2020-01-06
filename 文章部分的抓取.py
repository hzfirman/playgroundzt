import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import os

dynasty=["元代"]
file_list=[]
image_name=[]
link_list=[]
div=[]
next_link = "thread-1753221-695-1.html"  # 起始页
url = "https://bbs.artron.net/" + next_link
response = requests.get(url)
bsobj = BeautifulSoup(response.text, 'html.parser')
path="D:\\python\\test\\台北故宫\\"

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

def turn_to_page(next_link,path):#从起始页开始翻页
    while next_link is not None:
        url = "https://bbs.artron.net/" + next_link
        response = requests.get(url)
        bsobj = BeautifulSoup(response.text, 'html.parser')
        print("正在打印%s页的图片链接" % next_link)
        #get_div(bsobj,path)
        file_link=bsobj.find_all("img",{"file":re.compile("https")})
        file_count=0
        for link_tag in file_link:
            link=link_tag.attrs["file"]
            file_name=next_link+str(file_count)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
            response = requests.get(link, headers=headers)
            f = open(path + file_name+".jpg","wb")
            f.write(response.content)
            f.close()
            file_count+=1
        next_page = bsobj.find("a", {"class": "nxt"})  # 获取下一页的链接
        if "href" in next_page.attrs:#假如有下一页，就获取链接
            next_link = next_page.attrs["href"]#得到下一页的网址
            if next_link!="thread-1753221-753-1.html":
                continue
            else:
                print("文章部分已结束")
                break

turn_to_page(next_link,path)

