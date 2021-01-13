URL = "https://www.energytrend.com/solar/list-{}.html"
PAGES = range(1,968)
URLS = [URL.format(page) for page in PAGES]

import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
with open("title_date.csv","w") as fp:
    for url in tqdm(URLS):
        html = requests.get(url).text
        # save html
        soup = BeautifulSoup(html, features="html.parser")
        articles = soup.find_all("article")
        for article in articles:
            title = article.find("table").find("h1").find("a").text
            date = article.find("table").find("span", attrs={"class":"newsdate"}).text
            fp.write(title+"\t"+date+"\n")