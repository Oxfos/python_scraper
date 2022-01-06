from bs4 import BeautifulSoup
import csv  
import requests
import time

"""
Used variables:
coinPages: list containing html links to coin forecast pages
"""

# Starting calculation of execution time
start_time = time.time()

# Get all websites with predictions
with open('Long-Term Price Predictions 2021-2031.html', 'r') as fr:
    # read and parse content of coins_list
    coinsHtml = BeautifulSoup(fr, 'lxml')

# get the list of link to the coins forecast pages
links = coinsHtml.main.div.div.find_all('a')
coinPages = []
for link in links:
    coinPages.append(link.get('href'))

# Per link get the coin forecast table
# prepare list to host data
data = []

for link in coinPages:
    soup = BeautifulSoup(requests.get(link).text, 'lxml')
    # Add title row with crypto name to data
    first_row = ['Year','Mid-Year','Year-End']
    title = soup.find('h1')
    splitted = title.text.split()
    splitted = splitted[0] + splitted[1]
    first_row.append(splitted)
    data.append(first_row)
    # for each table row in all table rows get the data
    trows = soup.find_all('tr')
    # remove first row because already present
    trows.pop(0)
    for tr in trows:
        rowList = []
        for td in tr.find_all('td'):
            rowList.append(td.text)
        data.append(rowList)

# Adding data to quotes.csv file
with open('quotes.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the data
    writer.writerows(data)

# Preparing data for combo graph
combo = []
# first row
first_row = []
first_row.append(data[0][0])
for i in range(len(data)):
    if i % 13 == 0:
        first_row.append(data[i][3])
combo.append(first_row)
# second row
for r in range(12):
    row = []
    # year
    row.append(data[r+1][0])
    # growth
    for c in range(len(data)):
        if c % 13 == 0:
            row.append(data[c+1+r][3])
    combo.append(row)

# Writing combo to combo.csv
with open('combo.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the data
    writer.writerows(combo)

print(time.time()-start_time)