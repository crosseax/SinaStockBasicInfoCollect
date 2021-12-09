import utils_test as u
import concurrent.futures

# This file starts the whole program

def main():

    # prompt user to decide if showing result at the end
    ifShowComp = input("Show company names collected at the end? [Y/N] ")

    # asking for inputs for stock numbers
    beginNum = input("Please input the STARTING stock number: ")
    endNum = int(input("Please input the ENDING stock number: "))+1

    # creating a empty list as result container
    allCompanies = []

    # generating URLs lists
    allSinaURLs = u.sina_url_generator(beginNum, endNum)

    # multi-threading executing the web scrapping function
    with concurrent.futures.ThreadPoolExecutor () as executor:
        print("Running...")
        for i in executor.map(u.sina_web_info_getter, list(allSinaURLs)):
            try:
                if i:
                    allCompanies.append(i)
            except:
                pass

    # creating xlsx workbook
    u.creating_sina_workbook(allCompanies)

    # output to command based on user input
    if str(ifShowComp) == "Y" or str(ifShowComp) == "y":
        for comp in allCompanies:
            print (comp[0],comp[1],comp[2])

    # result output
    print (f"Numbers of companies' info collected: {len(allCompanies)}")
    print ("Excel Worksheet successfully created")
    print ("Done")

