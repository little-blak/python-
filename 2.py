# -*- coding:utf-8 -*--
import urllib.request
import xlwt
from bs4 import BeautifulSoup
import re
from io import BytesIO
import gzip

def mains():
    # 爬取网页
    baseurl = "https://hz.newhouse.fang.com/house/s/b"
    headers={
        "User-Agent" :"Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 84.0.4147.105 Safari / 537.36"
    }

    req=urllib.request.Request(url=baseurl,headers=headers)

    response = urllib.request.urlopen(req)


    dataList = getData(baseurl)

    savepath = ".\\豆瓣电影Top.xls"
    saveData(dataList, savepath)
findname=re.compile(r'<span>(\d*)</span>',)
findlink=re.compile(r'<a.*>([\s\S]*?)</a>')
findlinks=re.compile(r'<a.*tit.*>([\s\S]*?)</a>')
findarea=re.compile((r'<div class="house_type clearfix".*>([\s\S]*?)</div>'))
findlog=re.compile(r'<a.*href=".*".*>(.*?)</a>')
findhref=re.compile(r'<a.*href="(.*?)"')
findimgsrc=re.compile(r'<img.*src="(.*?)"',re.S)
findtitle=re.compile(r'<span class="title">(.*)</span>')
findrat=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findj=re.compile(r'<span>(\d*)人评价</span>')
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)
findmore=re.compile(r'<a.*href="(.*?)".*>')
findprice=re.compile(r'<em>(\d*)元/平方米</em>')
findle=re.compile(r'<div.*class="list-left".*>(.*?)</div>')
findr=re.compile(r'<div.*class="list-right".*>(.*?)</div>')
finds=re.compile(r'<li><span>.*?</span>([\s\S]*?)</li>')
findss=re.compile(r'<span class="tag">(.*?)</span>')
findname=re.compile(r'<a class="ts_linear".*>(.*?)</a>')
findalls=re.compile(r'<a.*href="(.*?)".*')
findtime=re.compile(r'<div.*class="list-right".*>(.*?)<a.*>.*开盘时间详情.*')

def getData(baseurl):
    links=[]

    data=[]
    for i in range(1,40):

        try:
            url=baseurl+"9"+str(i)
            html=askUrl(url)
            soup=BeautifulSoup(html,"html.parser")
        except:
            print(i)
            return dataLists
        for item in soup.find_all('div',class_="nlc_img"):
            print(1111)
            item=str(item)
            link=re.findall(findhref,item)[0]
            try:
                link = "https:" + link
                dataLists = main(link)
                print(main(link))
                data.append(dataLists)
                print(data)
            except:
                print("报错啦")
                links.append(link)
    print(link)

            # print(link)
    return data
# 解析数据
# 保存数据
def saveData(savepath):
    pass
def askUrl(url):
    headers={
        "User-Agent" :"Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 84.0.4147.105 Safari / 537.36"
    }

    req=urllib.request.Request(url=url,headers=headers)

    try:
        response = urllib.request.urlopen(req)
        # print(response.status)
        f = gzip.GzipFile(fileobj=response)
        html=f.read().decode('gbk')
        # print(response.read().decode('utf-8'))
    except url.error.URLError as e:
        return 0
        pass

    return html

def saveData(dataList,savepath):
    book=xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet=book.add_sheet('豆瓣小电影TOP250',cell_overwrite_ok=True)


    jj=len(dataList)
    for  i in range(0,jj-1):
        print("第%d条"%i)
        data=dataList[i]
        if(not data):
            continue
        print(data)
        for j in range(0,len(data)):
                sheet.write(i+1,j,data[j])
    book.save('students.xls')
def main(baseurl):
    # 爬取网页

    print(baseurl)
    headers={
        "User-Agent" :"Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 84.0.4147.105 Safari / 537.36"
    }

    req=urllib.request.Request(url=baseurl,headers=headers)
    # print(req)
    response = urllib.request.urlopen(req)
    # print(response.status)
    # print(response.read().decode('utf-8'))

    dataList = getDatas(baseurl)
    return dataList
    savepath = ".\\豆瓣电影Top.xls"
    # saveData(dataList, savepath)
def getDatas(baseurl):


    print("二级页面")
    try:
        url=baseurl
        html=askUrl(url)
    except:
        return

    soup=BeautifulSoup(html,"html.parser")

    for item in soup.find_all('div',class_="more"):
           # print(item)

            data=[]
            item=str(item)
            link=re.findall(findmore,item)[0]
            print(link)
            link="https:"+link

            print("样式一")
            dataList=mainss(link)
            return dataList


    for item in soup.find_all('div', class_="fn-line"):
        data=[]
        item=str(item)
        link=re.findall(findalls,item)[0]
        print(link)
        link="https:"+link

        print("样式二")
        dataList=mainss(link)
        return dataList





def mainss(baseurl):
    # 爬取网页

    print(baseurl)
    headers={
        "User-Agent" :"Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 84.0.4147.105 Safari / 537.36"
    }

    req=urllib.request.Request(url=baseurl,headers=headers)
    # print(req)
    response = urllib.request.urlopen(req)
    # print(response.status)
    # print(response.read().decode('utf-8'))

    dataList = getDatass(baseurl)
    savepath = ".\\111Top.xls"
    # saveData(dataList, savepath)
    return dataList
def getDatass(baseurl):
    dataList = []



    url=baseurl
    html=askUrl(url)
    soup=BeautifulSoup(html,"html.parser")
    for item in soup.find_all('body'):
        item = str(item)
        name=re.findall(findname,item)

    for item in soup.find_all('div',class_="main-left"):
            # print(item)

            data=[]
            item=str(item)
            data.append(name[0])
            if(re.findall(findprice,item)):
                link=re.findall(findprice,item)[0]
                data.append(link)
            else:
                data.append('未定价')
            print("三级页面")
            try:
                time=re.findall(findtime,item)[0]
                data.append(time)
                li = re.findall(findle, item)
                r = re.findall(findr, item)
                s = re.findall(finds, item)
                ss = re.findall(findss, item)
                if (r):

                    for i in range(0, len(r)):
                        data.append(r[i])

                    for ii in range(0, len(s)):
                        data.append(s[ii])
            except:
                li = re.findall(findle, item)
                r = re.findall(findr, item)
                s = re.findall(finds, item)
                ss = re.findall(findss, item)
                if (r):

                    for i in range(0, len(r)):
                        data.append(r[i])

                    for ii in range(0, len(s)):
                        data.append(s[ii])



    dataList.append(data)
    dataList=dataList[0]

    return dataList;

    return dataList
mains()
