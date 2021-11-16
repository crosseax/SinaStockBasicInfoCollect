import requests
from bs4 import BeautifulSoup
import chardet
import xlsxwriter
import concurrent.futures


def infinite_sequence(n, m): # number generator
    num = int(n)
    while num < int(m):
        yield "{:06n}".format(num)
        num += 1

def collecting_infos(url): # for this web in particular

    try:
        print ("Collecting data of {} ...".format(url.split("/")[5]))
        
        # acquiring datas and decoding
        data = requests.get(url)
        decoded = data.content.decode("GB18030") 
        soup = BeautifulSoup(decoded, "html.parser")

        # collecting info
        datas = []
        for tr in soup.find_all("div", {"class": "com_overview blue_d"}):
            datas.append("{}：{}".format("公司代码",url.split("/")[5]))
            for td in tr.find_all('p'):
                datas.append(td.text)
        for tr in soup.find_all('div', {'class': 'hq_title'}):
            for td in tr.find_all('h1'):
                datas.append(td.text)
        print ('Done collecting stock {} ...'.format(url.split('/')[5]))
        return (datas)

    except: 
        pass


def main():

    ifShowComp = input("Show company names collected at the end? [Y/N] ")

    # generating URLs
    stockURLs = []
    for num in infinite_sequence(input("Please input the STARTING stock number: "), int(input("Please input the ENDING stock number: "))+1):
        if num[0] != "6":
            num = "sz" + num
            stockURLs.append("https://finance.sina.com.cn/realstock/company/"+num+"/nc.shtml")
        else:
            num = "sh" + num
            stockURLs.append("https://finance.sina.com.cn/realstock/company/"+num+"/nc.shtml")
        stockURLs.append(str(num))


    # collecting information
    allCompanies = []
    with concurrent.futures.ThreadPoolExecutor () as executor:
        print("Running...")
        for i in executor.map(collecting_infos, stockURLs):
            try:
                if len(i) > 1:
                    allCompanies.append(i)
            except:
                pass

    # creating workbook
    print ("Creating xlsx and importing data...")
    outWorkbook = xlsxwriter.Workbook(r"./CompanyList.xlsx")
    outSheet = outWorkbook.add_worksheet()
    for row in range(len(allCompanies)):
        for col in range(len(allCompanies[0])):
            outSheet.write(row, col, allCompanies[row][col])
    outWorkbook.close()

    if str(ifShowComp) == "Y" or str(ifShowComp) == "y":
        for comp in allCompanies:
            print (comp[0],comp[1],comp[2])

    print ("Done")


if __name__ == "__main__":
    main()