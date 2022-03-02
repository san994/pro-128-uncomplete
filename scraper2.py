import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(START_URL)
time.sleep(10)

soup = BeautifulSoup(page.text,"html.parser")
table = soup.find_all("table")

temp_list = []
table_row = table[6].find_all("tr")
for tr_tag in table_row:
    td = tr_tag.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

star_name =[]
mass = []
radius = []
distance=[]

for i in range(1,len(temp_list)):
    star_name.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][8])
    radius.append(temp_list[i][9])
    #lum.append(temp_list[i][7])


df = pd.DataFrame(list(zip(star_name,distance,mass,radius)),columns=['star_name',"distance","mass","radius"])
df.to_csv("star_data.csv")