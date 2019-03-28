from datetime import datetime
import csv
import pandas as pd
from bs4 import BeautifulSoup
import requests

# page = requests.get(
#     "https://app.dutchbanglabank.com/DBBLWeb/ATMLocation")
# soup = BeautifulSoup(page.content, 'html.parser')

atm_container = ''
with open('test.txt', 'r') as f:
    for line in f:
        atm_container += line
        # print(line)
        # for word in line.split():
        #     print(word)

# print(atm_container)
dis_dhaka = atm_container.find(id="disDhaka")
print(dis_dhaka)

# print([type(item) for item in list(soup.children)])
# html = list(soup.children)[9]
# len = list(html.children).__len__()
# body = list(html.children)[len - 2]
# divs = body.find_all('div')
# print(divs)

# atm_container = soup.find(id="ctl00_cphBody_pnlATMContainer")
# dis_dhaka = atm_container.find(id="disDhaka")
# areas = dis_dhaka.find_all("div")
# print(areas[0]["id"])
# print(areas[0].find_all("td"))
# print(areas[0].select("tr td"))


# ATM = pd.DataFrame({
#     "Address": addresses,
#     "Area": areas,
#     "City": cities,
#     "Lat": lats,
#     "Lng": lngs,
#     "pType": ptypes,
#     "subType": subTypes,
#     "Post Code": postCodes
# })

# ATM["Time"] = datetime.now()

# with open('atm.csv', 'a') as csv_file:
#     weather.to_csv(csv_file, sep='\t', encoding='utf-8')
