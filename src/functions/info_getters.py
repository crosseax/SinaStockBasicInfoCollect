import requests
from bs4 import BeautifulSoup
from datetime import date


# number generator
def infinite_sequence(n, m):
    num = int(n)
    while num < int(m):
        yield "{:06n}".format(num)
        num += 1


# generates urls for sina stock websites
def sina_url_generator(beginNum, endNum):
    stockURLs = []
    prefix = "sz"
    for num in infinite_sequence(beginNum, endNum):
        if num[0] == "6":
            prefix = "sh"
        elif num[0] == "8" or num[0] == "4":
            prefix = "bj"
        stockURLs.append(f"https://finance.sina.com.cn/realstock/company/{prefix}{num}/nc.shtml")
    return stockURLs


# generates urls for xueqiu stock websites
def xueqiu_url_generator(beginNum, endNum):
    stockURLs = []
    prefix = "SZ"
    for num in infinite_sequence(beginNum, endNum):
        if num[0] == "6":
            prefix = "SH"
        elif num[0] == "8" or num[0] == "4":
            prefix = "BJ"
        stockURLs.append(f"https://xueqiu.com/S/{prefix}{num}")
    return stockURLs


# retrieve the information from sina web in particular
# takes a url, return a list of decoded information
def sina_web_info_getter(url): 
    try:
        print ("[Sina] Collecting data of {} ...".format(url.split("/")[5]))
        
        # acquiring datas and decoding
        data = requests.get(url)
        if data.status_code == 200 :
            decoded = data.content.decode("GB18030") 
            soup = BeautifulSoup(decoded, "html.parser")

            # collecting info
            datas = []
            for tr in soup.find_all("div", {"class": "com_overview blue_d"}):
                datas.append("{}：{}".format("公司代码", url.split("/")[5]))
                for td in tr.find_all('p'):
                    datas.append(td.text)
            for tr in soup.find_all('div', {'class': 'hq_title'}):
                for td in tr.find_all('h1'):
                    datas.append(td.text)
            print ('[Sina] Done collecting stock {} ...'.format(url.split('/')[5]))
            return (datas)

    except: 
        pass


# retrieve the information from xueqiu web in particular
# takes a url, return a list of decoded information
def xueqiu_web_info_getter(url): 
    today = date.today()
    try:
        print ("[Xueqiu] Collecting data of {} ...".format(url.split("/")[4]))
        
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}

        # acquiring datas and decoding
        data = requests.get(url, headers=headers)
        if data.status_code == 200 :
            decoded = data.content.decode("utf-8") 
            soup = BeautifulSoup(decoded, "html.parser")

            # collecting info
            datas = []
            for tr in soup.find_all("div", {"class": "stock-name"}):
                datas.append("{}：{}".format("日期", today.strftime("%Y/%m/%d")))
                datas.append("{}：{}".format("公司名称", tr.text.split('(')[0]))
                datas.append("{}：{}".format("公司代码", url.split("/")[4]))
            for tr in soup.find_all("div", {"class": "quote-container"}):
                for td in tr.find_all('td'):
                    datas.append(td.text)
            print ("[Xueqiu] Done collecting stock {} ...".format(url.split('/')[4]))
            return (datas)

    except: 
        pass