import setting
import scraping
import requests

message=scraping.message

TOKEN_F = setting.AP_F
TOKEN_GM = setting.AP_GM
TOKEN_N = setting.AP_N
TOKEN_Y = setting.AP_Y

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

if __name__ == "__main__":
    main()
