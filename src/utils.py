import requests
from bs4 import BeautifulSoup
import chardet
from requests.models import Response
import xlsxwriter
import concurrent.futures

# number generator
def infinite_sequence(n, m):
    num = int(n)
    while num < int(m):
        yield "{:06n}".format(num)
        num += 1


# generates urls for sina stock websites
def sina_url_generator(beginNum, endNum):
    stockURLs = []
    for num in infinite_sequence(beginNum, endNum):
        if num[0] == "6":
            num = "sh" + num
            stockURLs.append("https://finance.sina.com.cn/realstock/company/"+num+"/nc.shtml")
        elif num[0] == "8" or num[0] == "4":
            num = "bj" + num
            stockURLs.append("https://finance.sina.com.cn/realstock/company/"+num+"/nc.shtml")
        else:
            num = "sz" + num
            stockURLs.append("https://finance.sina.com.cn/realstock/company/"+num+"/nc.shtml")
    return stockURLs


# retrieve the information from sina web in particular
# takes a url, return a list of decoded information
def sina_web_info_getter(url): 
    try:
        print ("Collecting data of {} from Sina website ...".format(url.split("/")[5]))
        
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
            print ('Done collecting stock {} ...'.format(url.split('/')[5]))
            return (datas)

    except: 
        pass


# use collected info to create a workbook
def creating_workbook(allCompanies): 
    print ("Creating xlsx file and importing data...")
    outWorkbook = xlsxwriter.Workbook(r"./CompanyList.xlsx")
    outSheet = outWorkbook.add_worksheet()
    for row in range(len(allCompanies)):
        for col in range(len(allCompanies[0])):
            outSheet.write(row, col, allCompanies[row][col])
    outWorkbook.close()