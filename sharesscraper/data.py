import lxml
import requests
from datetime import datetime
from bs4 import BeautifulSoup

my_table_data = []
base_url = "https://trendlyne.com/portfolio/superstar-shareholders/index/"
page = requests.get(base_url)
soup = BeautifulSoup(page.content, 'lxml')
page_table = soup.find("div", class_="content-wrapper").find("div", class_="tl_carousel").find("div",
                                                                                               class_="scrolling-wrapper").find(
    "div", class_="row").find("div", class_="card")
page_rows = page_table.find_all("div", class_="dbdr")

for div in page_rows:
    splited_data = div.find("div", class_="col-lg-5").find("a").get("href").split('/')
    splited_data[4] = f"Q1-{datetime.today().year}"
    final_string = ""
    for foo in splited_data:
        final_string += f"/{foo}"
    my_table_data.append((
        div.find("div", class_="col-lg-5").find("a").text,  # The Name
        div.find_all("div", class_="col-lg-3")[1].text,  # The Net Worth
        div.find_all("div", class_="col-lg-3")[0].text,  # The Companies
        "https://trendlyne.com" + str(final_string)  # The detailed url
    ))

def detailed_data(url):
    print(url)

