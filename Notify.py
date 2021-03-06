import scraping
import requests
import os

message=scraping.message

TOKEN_F = os.environ.get("LINE_TOKEN_F")
TOKEN_Y = os.environ.get("LINE_TOKEN_Y")
TOKEN_N = os.environ.get("LINE_TOKEN_N")
TOKEN_GM = os.environ.get("LINE_TOKEN_GM")
# TOKEN_MINE = os.environ.get("LINE_TOKEN_MINE")

def main():
    send_line_notify_F(
      message
    )
    send_line_notify_GM(
      message
    )
    send_line_notify_N(
      message
    )
    send_line_notify_Y(
      message
    )
    # send_line_notify_ME(
    #   message
    # )



def send_line_notify_F(notification_message):
    """
    LINEに通知する
    """
    line_notify_token_F = TOKEN_F
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token_F}'}
    data = {'message': f'\n{notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)

def send_line_notify_GM(notification_message):
    """
    LINEに通知する
    """
    line_notify_token_GM = TOKEN_GM
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token_GM}'}
    data = {'message': f'\n{notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)

def send_line_notify_N(notification_message):
    """
    LINEに通知する
    """
    line_notify_token_N = TOKEN_N
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token_N}'}
    data = {'message': f'\n{notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)

def send_line_notify_Y(notification_message):
    """
    LINEに通知する
    """
    line_notify_token_Y = TOKEN_Y
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token_Y}'}
    data = {'message': f'\n{notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)
    
# def send_line_notify_ME(notification_message):
#     """
#     LINEに通知する
#     """
#     line_notify_token_MINE = TOKEN_MINE
#     line_notify_api = 'https://notify-api.line.me/api/notify'
#     headers = {'Authorization': f'Bearer {line_notify_token_MINE}'}
#     data = {'message': f'\n{notification_message}'}
#     requests.post(line_notify_api, headers = headers, data = data)


if __name__ == "__main__":
    main()
