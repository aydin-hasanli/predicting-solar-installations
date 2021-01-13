# URL = "https://www.energytrend.com/pricequotes/list-{}.html"
# PAGES = range(1,51)
# URLS = [URL.format(page) for page in PAGES]

# import requests
# from tqdm import tqdm
# from bs4 import BeautifulSoup
# with open("pricequotes_date.csv","w") as fp:
#     for url in tqdm(URLS):
#         html = requests.get(url).text
#         # save html
#         soup = BeautifulSoup(html, features="html.parser")
#         articles = soup.find_all("article")
#         for article in articles:
#             title = article.find("table").find("h1").find("a").text

#             date = article.find("table").find("span", attrs={"class":"newsdate"}).text
#             fp.write(title+"\t\t"+date+"\n")

URL = "https://www.energytrend.com/pricequotes/list-{}.html"
PAGES = range(31,51)
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
            article_url = article.find("table").find("h1").find("a")['href']
            # obtain and save the content of the link
            file_name = article_url.split("/")[-1]
            with open("solar/" + file_name, "w") as fp_artcile:
                artcile_html = requests.get(article_url).text
                fp_artcile.write(artcile_html)
            date = article.find("table").find("span", attrs={"class":"newsdate"}).text
            fp.write(title+"\t\t"+date+"\n")