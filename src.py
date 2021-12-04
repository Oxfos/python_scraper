from bs4 import BeautifulSoup

with open('BITCOIN PRICE PREDICTION 2021 - 2025 - 2030.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    tr = soup.find_all('tr')
    print(tr)