import requests
from bs4 import BeautifulSoup
import re
import urllib.request

dynasty=["元代"]
file_list=[]
image_name=[]
link_list=[]
div=[]
next_link = "thread-1753221-3-1.html"  # 起始页
url = "https://bbs.artron.net/" + next_link
response = requests.get(url)
bsobj = BeautifulSoup(response.text, 'html.parser')

def get_dynasty_name():
    image_dynasty_list = bsobj.find_all("font", {"size": "7"})
    if len(image_dynasty_list)!=0:
        print(image_dynasty_list[0].text)
        dynasty.append(image_dynasty_list)

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

#def saveimglinktofile():
#   next_link = "thread-1753221-1-1.html"#起始页
#   with open("元.txt","a") as age:#打开文件，以便于存储在文件中
#       while next_link is not None:
#           print("正在打印%s页的图片链接"%next_link)
#           url="https://bbs.artron.net/"+next_link
#           response = requests.get(url)
#           bsobj = BeautifulSoup(response.text, 'html.parser')
#           imagelocation = bsobj.find_all("img", {"file": re.compile("https://bbscache3*.artron.net/.*jpg")})#匹配所有图片的链接
#           for image_item in imagelocation:
#                if "file" in image_item.attrs:
#           #print(i.attrs["file"])
#                   yuan_link=image_item.attrs["file"]
#                   age.write(yuan_link+"\n")#把链接存储在文件中后回车
#           next_page = bsobj.find("a", {"class": "nxt"})#获取下一页的链接
#           if "href" in next_page.attrs:
#               next_link = next_page.attrs["href"]
#               print(next_link)

def get_file_name(div):
    image_name_list=div.find_all("font",{"size":re.compile("5|6")})
    for image in image_name_list:
        res=re.match('<font size=.*><font color="darkred">.*</font></font', str(image))
        if res is not None:
            name=dynasty[-1]+image.text.strip()
            print(name)
            image_name.append(name)
    return(image_name)

def downloadimgfiletodir():
    next_link = "thread-1753221-1-1.html"#起始页
    while next_link is not None:
        print("正在打印%s页的图片链接"%next_link)
        url="https://bbs.artron.net/"+next_link
        #response = requests.get(url)
        #bsobj = BeautifulSoup(response.text, 'html.parser')
        imagelocation = bsobj.find_all("img", {"file": re.compile("https://bbscache3*.artron.net/.*jpg")})#匹配所有图片的链接
        for image_item in imagelocation:
             if "file" in image_item.attrs:

                urllib.request.urlretrieve(yuan_link, 'D:\\python\\test\\%s' %img_name,Schedule)#把链接存储在文件中后回车
        next_page = bsobj.find("a", {"class": "nxt"})#获取下一页的链接
        if "href" in next_page.attrs:
            next_link = next_page.attrs["href"]
            print(next_link)

def get_div():
    div_list=bsobj.find_all("div",{"class","pcb"})
    for div in div_list:
        get_file_name(div)

downloadimgfiletodir()