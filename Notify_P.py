import bs4
import requests
import datetime
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

AP_MY = os.environ.get("LINE_TOKEN_MY")


Target_URL = 'https://covid19.codeforaomori.org/'
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
resp = requests.get(Target_URL, headers=headers)
resp.raise_for_status()
now = datetime.datetime.today().strftime('%Y年%m月%d日')
soup = bs4.BeautifulSoup(resp.text, "html.parser")
entries = soup.find_all(class_="DataView-Header")
number = entries[0].find(class_="DataView-DataInfo-summary").text.replace('人','').replace(' ','').replace('\n', '')
date = entries[0].find(class_="DataView-DataInfo-date").text
message = f'{now}の青森県の新規感染者数は\n{number}人\n({date})'
# print(f'{now}の青森県の新規感染者数は{number}人\n({date})')

TOKEN = AP_MY

def main():
    send_line_notify(
      message
    )

def send_line_notify(notification_message):
    """
    LINEに通知する
    """
    line_notify_token = TOKEN
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'\n{notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)

if __name__ == "__main__":
    main()