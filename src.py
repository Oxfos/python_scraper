from bs4 import BeautifulSoup
import csv  

# Get all websites with predictions
with open('Long-Term Price Predictions 2021-2031.html', 'r') as fr:
    # read and parse content of coins_list
    coinsHtml = BeautifulSoup(fr, 'lxml')

# get the list of links
links = coinsHtml.main.div.div.find_all('a')
for link in links:
    print(link.get('href'))



# Per link get the  coint forecast table

with open('BITCOIN PRICE PREDICTION 2021 - 2025 - 2030.html', 'r') as fr:
    # read and parse content of html_file
    soup = BeautifulSoup(fr, 'lxml')

# prepare list to host data
data = []
# find all table rows
tableRows = soup.find_all('tr')
# for each table row
for tr in tableRows:
    rowList = []
    rowData = tr.find_all('td')
    for td in rowData:
        rowList.append(td.text)
    data.append(rowList)

# Add title to data
title = soup.find('h1')
data[0][3] = title.text.split()[0]

# Adding data to csv file
with open('quotes.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the data
    writer.writerows(data)
