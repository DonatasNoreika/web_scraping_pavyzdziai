import csv
from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.telia.lt/prekes/mobilieji-telefonai/samsung').text
soup = BeautifulSoup(source, 'html.parser')

with open("telia_telefonai.csv", 'w', encoding="UTF-8", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['PAVADINIMAS', 'MĖNESIO KAINA', 'KAINA'])
    blokai = soup.find_all('div', class_='mobiles-product-card card card__product card--anim js-product-compare-product')
    for blokas in blokai:
        pavadinimas = blokas.find('a', class_="mobiles-product-card__title js-open-product").get_text().strip()
        men_kaina = blokas.find('div', class_="mobiles-product-card__price-marker").get_text().strip()
        kaina = blokas.find_all('div', class_='mobiles-product-card__price-marker')[1].get_text().strip()
        csv_writer.writerow([pavadinimas, men_kaina, kaina])
        print(pavadinimas, men_kaina, kaina)
