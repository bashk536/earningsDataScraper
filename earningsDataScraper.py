import requests
import csv
from bs4 import BeautifulSoup as bs
from itertools import islice

with open("snp500.txt", "r") as r:
    tickers = [x.rstrip('\n') for x in r]

for ticker in tickers[288:289]:
    #Load webpage contents
    wp = requests.get("https://finance.yahoo.com/calendar/earnings?symbol={0}".format(str(ticker)))

    #Convert to beautiful soup object
    soup = bs(wp.content, "html.parser")


    table = soup.table
    allRows = table.find_all("tr")
    rows = allRows[10:14]

    data = []
    data2 = []
    flag = True
    with open("erData.csv", "a", newline="") as f:
        csv_writer = csv.writer(f)
        for row in rows:
            cell_iter = iter(row)
            for cell in cell_iter:
                if(flag):
                    next(islice(cell_iter, 2))
                    flag = False
                    continue
                cellData = cell.text
                data.append(cellData)
            flag = True
        data2.append(data)
            
        csv_writer.writerows(data2)
    wp.close()
r.close()
f.close()
