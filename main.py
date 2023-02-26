from urllib.parse import urlparse
import argparse
import requests
import os
from dotenv import load_dotenv


def shorten_link(token, user_input):
    headers = {"Authorization": token}
    payload = {"long_url": user_input}
    url = 'https://api-ssl.bitly.com/v4/shorten'
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    bitlink = response.json()['link']
    return bitlink


def count_clicks(token, parsed_link):
    headers = {"Authorization": token}
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{0}/clicks/summary'.format(parsed_link)
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    clicks = response.json()['total_clicks']
    return "Переходов по ссылке: {0}".format(clicks)


def is_bitlink(parsed_link):
    token = os.getenv('BITLY_TOKEN')
    headers = {"Authorization": token}
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{0}'.format(parsed_link)
    response = requests.get(url, headers=headers)
    return response.ok

def getting_link():
    parser = argparse.ArgumentParser(
        description='Получние битлинка'
    )
    parser.add_argument('link', help='Ваша ссылка')
    args = parser.parse_args()
    return args.link


def main():
    load_dotenv()
    token = os.getenv('BITLY_TOKEN')
    user_input = getting_link()
    parsed_result = urlparse(user_input)
    parsed_link = f"{parsed_result.netloc}{parsed_result.path}"
    try:
        if is_bitlink(parsed_link):
            print(count_clicks(token, parsed_link))
        else:
            print(shorten_link(token, user_input))
    except requests.exceptions.HTTPError:
        print("Ошибка!")


if __name__ == '__main__':
    main()
