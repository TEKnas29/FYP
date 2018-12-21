from lxml import html
import csv
import os
import urllib3
import requests
import re
import sqlite3
requests.packages.urllib3.disable_warnings()

#visit
nam = input('Enter Game :')
url = 'https://store.steampowered.com/search/?term='+nam
htmltext = requests.get(url).content.decode('utf-8')
print('processing:\n'+ url)
response = requests.get(url, verify=False)

#scan function
doc = html.fromstring(response.content)
Sturl = doc.xpath('//*[@id="search_result_container"]/div[2]/a[1]//@href')
Stcode = Sturl[0].split('/')
print(Stcode[4])

#re-visit
St = 'https://store.steampowered.com/app/'+Stcode[4]+'/' + Stcode[5]
htmltext = requests.get(St).content.decode('utf-8')
print('processing:\n'+ St)
response = requests.get(St, verify=False)

#Data
doc = html.fromstring(response.content)
#rec = doc.xpath('//*[conatains(@class,"discount_final_price")]//text()')
rec = doc.xpath('//*[@id="game_area_purchase"]/div[1]/div/div[2]/div/div[1]/div[2]/div[2]')
print(rec)