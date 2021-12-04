from bs4 import BeautifulSoup
import csv  
import requests

"""
Used variables:
coinPages: list containing html links to coin forecast pages
"""

# Get all websites with predictions
with open('Long-Term Price Predictions 2021-2031.html', 'r') as fr:
    # read and parse content of coins_list
    coinsHtml = BeautifulSoup(fr, 'lxml')

# get the list of link to the coins forecast pages
links = coinsHtml.main.div.div.find_all('a')
coinPages = []
for link in links:
    coinPages.append(link.get('href'))

# Get the content of the page
coinPages = ['https://coinpriceforecast.com/bitcoin-forecast-2020-2025-2030','https://coinpriceforecast.com/ethereum-forecast-2020-2025-2030']


# Per link get the coin forecast table
# prepare list to host data
data = []

for link in coinPages:
    requests.get(link)
    """
    with open(link, 'r') as fr:
        # read and parse content of html_file
        soup = BeautifulSoup(fr, 'lxml')
    """
    soup = BeautifulSoup(requests.get(link).text, 'lxml')
    # Add title row to data with crypto name
    first_row = 'Year,Mid-Year,Year-End,'
    title = soup.find('h1')
    data.append([first_row + title.text.split()[0]])
    # for each table row in all table rows get the data
    trows = soup.find_all('tr')
    trows.pop(0)
    for tr in trows:
        rowList = []
        for td in tr.find_all('td'):
            rowList.append(td.text)
        data.append(rowList)



# Adding data to csv file
with open('quotes.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the data
    writer.writerows(data)
