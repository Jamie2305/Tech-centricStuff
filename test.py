import requests
from bs4 import BeautifulSoup

with open("partlist.txt","r") as f:
    URLS = f.read().replace(" ","").split("\n")

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}


for URL in URLS:
    page=requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    section=soup.find("div",id="prices")

    cols=section.tbody

    prices=cols.find_all("tr")

    for price in prices:

        buy_link=price.a["href"]
        buy_link="uk.pcpartpicker.com"+buy_link

        print(price.find("td",class_="td__finalPrice").text)
    
