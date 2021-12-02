import requests
from bs4 import BeautifulSoup
import chardet
import xlsxwriter
import concurrent.futures

# number generator
def infinite_sequence(n, m):
    num = int(n)
    while num < int(m):
        yield "{:06n}".format(num)
        num += 1


# returns a list of all urls
def url_generator():
    # generating URLs according to input
    beginNum = input("Please input the STARTING stock number: ")
    endNum = int(input("Please input the ENDING stock number: "))+1
    stockURLs = []
    for num in infinite_sequence(beginNum, endNum):
        if num[0] != "6":
            num = "sz" + num
            stockURLs.append("https://finance.sina.com.cn/realstock/company/"+num+"/nc.shtml")
        else:
            num = "sh" + num
            stockURLs.append("https://finance.sina.com.cn/realstock/company/"+num+"/nc.shtml")
    return stockURLs


# retrieve the information from sina web in particular
# takes a url, return a list of decoded information
def sina_web_getter(url): 
    try:
        print ("Collecting data of {} ...".format(url.split("/")[5]))
        
        # acquiring datas and decoding
        data = requests.get(url)
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
        print ('Done collecting stock {} ...'.format(url.split('/')[5]))
        return (datas)

    except: 
        pass



