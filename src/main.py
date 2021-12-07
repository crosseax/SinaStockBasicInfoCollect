import utils as u
import concurrent.futures

# This file starts the whole program

def main():

    # prompt user to decide if showing result at the end
    ifShowComp = input("Show company names collected at the end? [Y/N] ")

    # asking for inputs for stock numbers
    beginNum = input("Please input the STARTING stock number: ")
    endNum = int(input("Please input the ENDING stock number: "))+1

    # creating a empty list as result container
    sinaStockInfo = []

    # generating URLs lists
    allSinaURLs = u.sina_url_generator(beginNum, endNum)

    # multi-threading executing the web scrapping function
    with concurrent.futures.ThreadPoolExecutor () as executor:
        print("Running...")
        for i in executor.map(u.sina_web_info_getter, allSinaURLs):
            try:
                if i:
                    sinaStockInfo.append(i)
            except:
                pass

    # creating xlsx workbook
    u.creating_workbook(sinaStockInfo)

    # output to command based on user input
    if str(ifShowComp) == "Y" or str(ifShowComp) == "y":
        u.showSinaInfo(sinaStockInfo)

    # result output
    print (f"Numbers of companies' info collected: {len(sinaStockInfo)}")
    print ("Excel Worksheet successfully created")
    print ("Done")

