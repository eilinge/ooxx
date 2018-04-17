import urllib.request
import os
import json

def url_open(url):
    req = urllib.request.Request(url)
    
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400')
    
    response = urllib.request.urlopen(url)
    
    html = response.read()

    print('a1')

    return html

def get_page(url):
    
    html=url_open(url).decode('utf-8')
    #html=url_open(url)
    print('html',html)

    a = html.find('current-comment-page')+23
    b = html.find(']',a)

    print('html[a:b]',html[a:b])
    return html[a:b]

def find_imgs(url):
    
    html = url_open(url).decode('utf-8')
    
    img_addrs = []

    a= html.find('img src=')
    print('a')
    
    #new_addrs = [] 
    while a != -1:
        b= html.find('.jpg', a,a+255)
        if b != -1:
            img_addrs.append(html[a+9:b+4])
        else:
            b = a+9

        a = html.find('img src=',b)

    return img_addrs

    
def save_imgs(folder,img_addrs):

    for each in img_addrs:
        print(each)
        
        filename = each.split('/')[-1]
        print('filename',filename)
        with open(filename,'wb')  as  f:
            img = url_open(each)
            f.write(img)
                  
def download_mm(folder= 'OOXX',pages = 2):
    #新建文件，切换文件目录
    try:
        os.mkdir('OOXX')
    except FileExistsError:
        pass
    os.chdir(folder)
    
    #url = 'http://jandan.net/ooxx/'
    url = 'http://pic.sogou.com/pics/recommend?'

    page_num = int(get_page(url))

    print('page_num',page_num)

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-'+ str(page_num) + '#comments'
#获取列表
        img_addrs = find_imgs(page_url)

        print('img_addrs',img_addrs)

        save_imgs(folder,img_addrs)

if __name__=='__main__':
    download_mm()
