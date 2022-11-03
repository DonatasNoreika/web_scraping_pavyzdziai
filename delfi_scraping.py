from bs4 import BeautifulSoup
import requests
import csv
import re

source = requests.get('https://www.delfi.lt/').text
soup = BeautifulSoup(source, 'html.parser')
blocks = soup.find_all('div', class_="headline")

with open("delfi_straipsniai.csv", 'w', encoding="UTF-8", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['CATEGORY', 'TEXT', 'LINK'])

    for block in blocks:
        try:
            category = block.find('div', class_='headline-category').get_text().strip()
            text = block.find('a', class_="CBarticleTitle").get_text()
            link = block.find('a', class_="CBarticleTitle")['href']
            csv_writer.writerow([category, text, link])
            print("-----------------------------------------")
            print(category)
            print(text)
            print(link)
        except:
            pass