# import requests
# import chardet
# import concurrent.futures
import xlsxwriter
# from bs4 import BeautifulSoup
# from datetime import date


# use collected info to create a Sina Stock workbook
def creating_sina_workbook(allCompanies): 
    print ("Creating xlsx file and importing Sina Stock data...")
    outWorkbook = xlsxwriter.Workbook(r"./SinaCompanyList.xlsx")
    outSheet = outWorkbook.add_worksheet()
    for row in range(len(allCompanies)):
        for col in range(len(allCompanies[0])):
            outSheet.write(row, col, allCompanies[row][col])
    outWorkbook.close()

# use collected info to create a Sina Stock workbook
def creating_xueqiu_workbook(allCompanies): 
    print ("Creating xlsx file and importing Xueqiu data...")
    outWorkbook = xlsxwriter.Workbook(r"./XueqiuCompanyList.xlsx")
    outSheet = outWorkbook.add_worksheet()
    
    titles = []
    for title in allCompanies[0]:
        title = title.split('：')[0]
        titles.append(title)
    print (titles)

    for col in range(len(titles)):
        outSheet.write(0, col, titles[col])

    for row in range(len(allCompanies)):
        for col in range(len(allCompanies[0])):
            outSheet.write(row+1, col, allCompanies[row][col].split('：')[1])
    
    outWorkbook.close()