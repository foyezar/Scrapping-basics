
# from bs4 import BeautifulSoup
# import requests
# page = requests.get(
#     "http://dataquestio.github.io/web-scraping-pages/simple.html")
# print(page.content)

# soup = BeautifulSoup(page.content, 'html.parser')

# ======================================== Find Using Tags ====================================================================
# print(soup.prettify())
# print(list(soup.children))
# print([type(item) for item in list(soup.children)])
# html = list(soup.children)[2]
# print(list(html.children))
# body = list(html.children)[3]
# print(body)
# p = list(body.children)[1]
# print(p.get_text())

# soup.find('p')
# print(soup.find_all('p')[0].get_text())

# =========================================== Find Using ID & Class ============================================================
# page = requests.get(
#     "http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
# soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.find_all('p', class_='outer-text'))
# print(soup.find_all(class_="outer-text"))

# import libraries
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# print(soup.find_all(id="first"))

# ================================================= Using CSS Selectors ==============================================================
# print(soup.select("div p"))

# # specify the url
# quote_page = 'http://www.bloomberg.com/quote/SPX:IND'

# # query the website and return the html to the variable ‘page’
# page = urlopen(quote_page, timeout=1)
# # print(page.read())

# # parse the html using beautiful soup and store in variable `soup`
# soup = BeautifulSoup(page, 'html.parser')

# # Take out the <div> of name and get its value
# # name_box = soup.find('h1', attrs={'class': 'companyName__99a4824b'})
# # name = name_box.text.strip()
# # print(name_box)
# # name_box = soup.find_all('h1')
# # print(name_box)
# # print([type(item) for item in list(soup.children)])
# html = list(soup.children)[2]
# # print(list(html.children))
# body = list(html.children)[3]
# # print(body)
# divs = body.find('div', attrs={'class': 'root'})
# print(html)

# get the index price
# price_box = soup.find('div', attrs={'class': 'priceText__1853e8a5'})
# price = price_box.text
# print(price)

# ========================================================= WEATHER DATA ==========================================================
from datetime import datetime
import csv
import pandas as pd
from bs4 import BeautifulSoup
import requests

page = requests.get(
    "http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')

seven_day = soup.find(id="seven-day-forecast")
# forecast_items = seven_day.find_all(class_="tombstone-container")
# tonight = forecast_items[0]
# print(tonight.prettify())

# period = tonight.find(class_="period-name").get_text()
# img = tonight.find('img')
# desc = img['title']
# short_desc = tonight.find(class_="short-desc").get_text()
# temp = tonight.find(class_="temp").get_text()

# print(period)
# print(desc)
# print(short_desc)
# print(temp)

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [period.get_text() for period in period_tags]

short_descs = [sd.get_text()
               for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [temp.get_text()
         for temp in seven_day.select(".tombstone-container .temp")]
descs = [desc['title']
         for desc in seven_day.select(".tombstone-container img")]
# print(periods)
# print(short_descs)
# print(temps)
# print(descs)

weather = pd.DataFrame({
    "Period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc": descs
})
# print(weather)

temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')

is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night
weather["Time"] = datetime.now()

# print(temp_nums)
# print(weather["temp_num"].mean())

# print(weather)


# open a csv file with append, so old data will not be erased
# with open('index.csv', 'a') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow([name, price, datetime.now()])

with open('index.csv', 'a') as csv_file:
    weather.to_csv(csv_file, sep='\t', encoding='utf-8')

# =================================================== Ductch Bangla Bank ========================================================
# from bs4 import BeautifulSoup
# import requests

# page = requests.get(
#     "https://app.dutchbanglabank.com/DBBLWeb/BranchLocation")
# soup = BeautifulSoup(page.content, 'html.parser')


# print(soup.find_all('p', class_='outer-text'))
# print(soup.find_all(class_="outer-text"))

# print(list(soup.children))
# print([type(item) for item in list(soup.children)])
# html = list(soup.children)[2]
# print(html)
# len = list(html.children).__len__()
# body = list(html.children)[len - 2]
# divs = body.find_all('div')
# print(divs)
# body = list(html.children)[3]
# print(body)
# p = list(body.children)[1]
# print(p.get_text())

# soup.find('p')
# print(soup.find_all('p')[0].get_text())
