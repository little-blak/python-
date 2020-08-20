# -*- coding:utf-8 -*--
import urllib.request
import xlwt
from bs4 import BeautifulSoup
import re
def mains():
    # 爬取网页
    baseurl = "https://movie.douban.com/top250?start="
    headers={
        "User-Agent" :"Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 84.0.4147.105 Safari / 537.36"
    }

    req=urllib.request.Request(url=baseurl,headers=headers)
    # print(req)
    response = urllib.request.urlopen(req)
    # print(response.status)
    # print(response.read().decode('utf-8'))

    dataList = getData(baseurl)
    savepath = ".\\豆瓣电影Top.xls"
    # saveData(dataList, savepath)

findlink=re.compile(r'<a href="(.*?)">')
findimgsrc=re.compile(r'<img.*src="(.*?)"',re.S)
findtitle=re.compile(r'<span class="title">(.*)</span>')
findrat=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findj=re.compile(r'<span>(\d*)人评价</span>')
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)

def getData(baseurl):
    dataList = []
    for i in range(0,10):
        url=baseurl+str(i*25)

        html=askUrl(url)


        soup=BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):

            data=[]
            item=str(item)
            link=re.findall(findlink,item)[0]
            data.append(link)
            img = re.findall(findimgsrc, item)[0]
            data.append(img)
            tit=re.findall(findtitle,item)

            if (len(tit)==2):

                ctitle=tit[0]
                data.append(ctitle)
                otitle=tit[1].replace("/","")
                data.append(otitle)
            else:
                data.append(tit[0])
                data.append(' ')
            rat=re.findall(findrat,item)[0]
            data.append((rat))
            rating=re.findall(findj,item)[0]
            data.append(rating)
            bd=re.findall(findBd,item)[0]
            data.append(bd)
            dataList.append(data)
    print(len(dataList))
    print(dataList)


    return dataList



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
        html=response.read().decode('utf-8')
        # print(response.read().decode('utf-8'))
    except url.error.URLError as e:
        if hasattr(e,"code"):
                print(e.code)
        if hasattr(e,"resason"):
            print(e.resason)
    return html

def saveData(dataList,savepath):
    book=xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet=book.add_sheet('豆瓣小电影TOP250',cell_overwrite_ok=True)
    col=('电影详情链接','图片链接','影片中文名','影片外国名','评分','评价数','详细信息')
    for i in range(0,6):
        sheet.write(0,i,col[i])
    for  i in range(0,250):
        print("第%d条"%i)
        data=dataList[i]
        for j in range(0,6):
            sheet.write(i+1,j,data[j])
    book.save('student.xls')
mains()
