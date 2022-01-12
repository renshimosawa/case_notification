import bs4
import requests
import datetime

Target_URL = 'https://www.pref.aomori.lg.jp/soshiki/kenko/hoken/covid19-press.html'
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
resp = requests.get(Target_URL, headers=headers)
resp.raise_for_status()
now = datetime.datetime.today().strftime('%Y年%m月%d日')
soup = bs4.BeautifulSoup(resp.text, "html.parser")
entries = soup.find_all(class_="bc")
table = entries[0].find(class_="textleft").text
tdlist = table.split("\n")
for text in tdlist:
   if "月" in text:
       date = text
for text in tdlist:
   if "感染症患者" in text:
       case = text.replace('新型コロナウイルス感染症患者（', '').replace('例）を確認', '')

message = f'{date}公表\n青森県新規感染者数　{case}人\n詳細:https://www.pref.aomori.lg.jp/soshiki/kenko/hoken/covid19-press.html'
print(message)