import utils as u
import concurrent.futures

# This file starts the whole program

def main():
    ifShowComp = input("Show company names collected at the end? [Y/N] ")

    # generating URLs lists
    allURLs = u.url_generator()

    allCompanies = []

    # multi-threading executing the web scrapping
    with concurrent.futures.ThreadPoolExecutor () as executor:
        print("Running...")
        for i in executor.map(u.sina_web_getter, allURLs):
            try:
                if i:
                    allCompanies.append(i)
            except:
                pass


    # creating workbook
    print ("Creating xlsx file and importing data...")
    outWorkbook = u.xlsxwriter.Workbook(r"./CompanyList.xlsx")
    outSheet = outWorkbook.add_worksheet()
    for row in range(len(allCompanies)):
        for col in range(len(allCompanies[0])):
            outSheet.write(row, col, allCompanies[row][col])
    outWorkbook.close()

    # output to command based on user input
    if str(ifShowComp) == "Y" or str(ifShowComp) == "y":
        for comp in allCompanies:
            if comp != None:
                print (comp[0], comp[1], comp[2])

    # result output
    print (f"Numbers of companies' info collected: {len(allCompanies)}")
    print ("Excel Worksheet successfully created")
    print ("Done")

