import csv
from bs4 import BeautifulSoup
import requests

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

csv_filename = 'drumsticks.csv'

with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Product', 'Info', 'Price', 'Link'])

    for i in range(1,11):
        url = "https://blastbeat-shop.ru/drumsticks?page={}".format(i)
        request = requests.get(url, headers = headers)
        soup = BeautifulSoup(request.text, "html.parser")
        product = soup.find_all("div", class_="good-block")

        for products in product:
            products = products.find("a", {'class':'good-name'} )
            link = products.get('href')
            info = products.findNext("a", {'class':'good-info'})
            price = products.findNext("span", {'class':'good-prise'})

            product_text = products.text.strip()
            info_text = info.text.strip()
            price_text = price.text.strip()
            link_text = link.strip()
            
            print(product_text, price_text, info_text, link_text)
        
            csv_writer.writerow([product_text, price_text, info_text, link_text])
