import bs4
import time
import requests
import datetime
import setting
import schedule
import csv


Target_URL = 'https://covid19.codeforaomori.org/'
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
resp = requests.get(Target_URL, headers=headers)
resp.raise_for_status()
now = datetime.datetime.now().strftime('%Y年%m月%d日')
soup = bs4.BeautifulSoup(resp.text, "html.parser")
articles=[] 

table = soup.find_all(class_="v-data-table__wrapper")[4]

r = [] 
thead = table.find('thead')
ths = thead.tr.find_all('th')
for th in ths:
  r.append(th.text)

articles.append(r)

tbody = table.find("tbody")
trs = tbody.find_all('tr')
for tr in trs:
  r = []
  for td in tr.find_all('td'):
    r.append(td.text)
  articles.append(r)

print(articles[0,3])

# for r in articles:
#   print(','.join(r))
# tr = body.find("tr")
# message = f'今日の{entries[4].find(class_="mode-label").text}の価格は{entries[4].find(class_="price").text}円です'
# TOKEN = setting.AP_F

# def main():
#     send_line_notify(
#       message
#     )

# def send_line_notify(notification_message):
#     """
#     LINEに通知する
#     """
#     line_notify_token = TOKEN
#     line_notify_api = 'https://notify-api.line.me/api/notify'
#     headers = {'Authorization': f'Bearer {line_notify_token}'}
#     data = {'message': f'\n{notification_message}'}
#     requests.post(line_notify_api, headers = headers, data = data)

# if __name__ == "__main__":
#     main()

# schedule.every().day.at("08:00").do(main, send_line_notify)

# while True:
#     schedule.run_pending()
#     time.sleep(3)