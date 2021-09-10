from bs4 import BeautifulSoup
import requests
import datetime
import setting
import csv
import os
import sys
import pandas as pd

Target_URL = 'https://covid19.codeforaomori.org/'
resp = requests.get(Target_URL)
soup = BeautifulSoup(resp.text, "html.parser")
# now = datetime.datetime.today().strftime('%Y年%m月%d日')
entries = soup.find_all(class_="DataView-Header")
# number = entries[0].find(class_="DataView-DataInfo-summary").text.replace('人','').replace(' ','').replace('\n', '')
# date = entries[0].find(class_="DataView-DataInfo-date").text
# headers = ['Today','Number','Date']
# message = f'{now}の青森県の新規感染者数は\n{number}人\n({date})'
# print(number)
result=[]
for data in entries:
  now = datetime.datetime.today().strftime('%Y年%m月%d日')
  number = entries[0].find(class_="DataView-DataInfo-summary").text.replace('人','').replace(' ','').replace('\n', '')
  date = entries[0].find(class_="DataView-DataInfo-date").text
  result.append([now, number, date])

print(result)
f = open("last_log.csv", "w", encoding='utf_8')
writecsv = csv.writer(f, lineterminator='\n')
writecsv.writerow(result)

def read_csv():
    if not os.path.exists('last_log.csv'):
        raise Exception('ファイルがありません。')
    if os.path.getsize('last_log.csv') == 0:
        raise Exception('ファイルの中身が空です。')
    csv_list = pd.read_csv('last_log.csv', header=None).values.tolist()
    return csv_list

def list_diff(result, last_result):
    return_list = []
    for tmp in result:
        if tmp not in last_result:
            return_list.append(tmp)
    return return_list
# f.close()
# print(date)
# with open('last_log.csv', 'w', newline='',encoding='utf_8') as file:
#   writer = csv.writer(file)
#   # writer.writerow(headers)
#   for entries in soup.find_all(class_='DataView-Header'):
#     now = datetime.datetime.today().strftime('%Y年%m月%d日')
#     number = entries[0].find(class_="DataView-DataInfo-summary").text.replace('人','').replace(' ','').replace('\n', '')
#     date = entries[0].find(class_="DataView-DataInfo-date").text
#     row=[now, number, date]
#     writer.writerow(row)

# def read_csv():
#     if not os.path.exists('last_log.csv'):
#         raise Exception('ファイルがありません。')
#     if os.path.getsize('last_log.csv') == 0:
#         raise Exception('ファイルの中身が空です。')
#     csv_list = pd.read_csv('last_log.csv', header=None).values.tolist()
#     return csv_list

# def list_diff(result, last_result):
#     return_list = []
#     for tmp in result:
#         if tmp not in last_result:
#             return_list.append(tmp)
#     return return_list

# TOKEN_ME = setting.AP_ME

# def main():
#     send_line_notify_ME(
#       message
#     )
    

# def send_line_notify_ME(diff_list):
#     """
#     LINEに通知する
#     """
#     line_notify_token = TOKEN_ME
#     line_notify_api = 'https://notify-api.line.me/api/notify'
#     headers = {'Authorization': f'Bearer {line_notify_token}'}
#     data = {'message': f'\n{notification_message}'}
#     requests.post(line_notify_api, headers = headers, data = data)
