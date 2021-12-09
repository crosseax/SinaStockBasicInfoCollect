import functions.utilities as u
import functions.info_getters as gtr
import functions.worksheet_creators as ws
import concurrent.futures


# This file starts the whole program

def main():

    # prompt user to decide if showing result at the end
    ifShowComp = input("Show company names collected at the end? [Y/N] ")
    ifSinaStock = input("Collecting Sina Stock info? (Basic company infos) [Y/N] ")
    ifXueqiuStock = input("Collecting Xueqiu Stock info? (Price info for today) [Y/N] ")

    # asking for inputs for stock numbers
    beginNum = input("Please input the STARTING stock number: ")
    endNum = int(input("Please input the ENDING stock number: "))+1

    # creating a empty list as result container
    sinaStockInfo = []
    xueqiuStockInfo = []

    # generating URLs lists
    allSinaURLs = gtr.sina_url_generator(beginNum, endNum)
    allXueqiuURLs = gtr.xueqiu_url_generator(beginNum, endNum)

    # multi-threading executing the sina web scrapping function
    if str(ifSinaStock) == "Y" or str(ifSinaStock) == "y":

        with concurrent.futures.ThreadPoolExecutor () as executor:
            print("Running...")
            for i in executor.map(gtr.sina_web_info_getter, list(allSinaURLs)):
                try:
                    if i:
                        sinaStockInfo.append(i)
                except:
                    pass

        ws.creating_sina_workbook(sinaStockInfo)



    # multi-threading executing the xueqiu web scrapping function
    if str(ifXueqiuStock) == "Y" or str(ifXueqiuStock) == "y":
        with concurrent.futures.ThreadPoolExecutor () as executor:
            print("Running...")
            for i in executor.map(gtr.xueqiu_web_info_getter, list(allXueqiuURLs)):
                try:
                    if i:
                        xueqiuStockInfo.append(i)
                except:
                    pass

        ws.creating_xueqiu_workbook(xueqiuStockInfo)



    # output to command based on user input
    if str(ifShowComp) == "Y" or str(ifShowComp) == "y":
        u.showSinaInfo(sinaStockInfo)
        print()
        u.showXueqiuInfo(xueqiuStockInfo)
        print()
        

    # result output
    print ("============")
    print (f"Numbers of Sina companies' info collected: {len(sinaStockInfo)}")
    print (f"Numbers of Xueqiu companies' info collected: {len(xueqiuStockInfo)}")
    print ("============")
    print ("Excel Worksheet successfully created")
    print ("Done")

