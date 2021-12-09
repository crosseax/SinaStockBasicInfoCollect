import utils_test as u
import concurrent.futures

# This file starts the whole program

def main():

    ifShowComp = input("Show company names collected at the end? [Y/N] ")

    beginNum = input("Please input the STARTING stock number: ")
    endNum = int(input("Please input the ENDING stock number: "))+1

    allCompanies = []

    allSinaURLs = u.sina_url_generator(beginNum, endNum)

    u.sina_multithreading_executor(allSinaURLs, allCompanies)

    u.creating_sina_workbook(allCompanies)

    if str(ifShowComp) == "Y" or str(ifShowComp) == "y":
        for comp in allCompanies:
            print (comp[0],comp[1],comp[2])

    print (f"Numbers of companies' info collected: {len(allCompanies)}")
    print ("Excel Worksheet successfully created")
    print ("Done")

