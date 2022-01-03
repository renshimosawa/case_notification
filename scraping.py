import bs4
import requests
import datetime

Target_URL = 'https://stopcovid19.pref.aomori.lg.jp/'
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
resp = requests.get(Target_URL, headers=headers)
resp.raise_for_status()
now = datetime.datetime.today().strftime('%Y年%m月%d日')
soup = bs4.BeautifulSoup(resp.text, "html.parser")
entries = soup.find_all(class_="DataView-Inner")
number = entries[0].find(class_="DataView-DataInfo-summary").text.replace('人','').replace(' ','').replace('\n', '')
date = entries[0].find(class_="DataView-DataInfo-date").text.replace('実績値','')
latest = entries[0].find(class_="Permalink").text.replace(' ','').replace('\n', '')

message = f'{now}の青森県の新規感染者数は\n{number}人{date}\n{latest}\n詳細:https://stopcovid19.pref.aomori.lg.jp/'
print(message)