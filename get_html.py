import requests
from choose_headers_randomly import choose_headers_randomly


def get_html(url):
    response = requests.get(url, headers=choose_headers_randomly())
    if response.status_code == 200:
        return response.text
    else:
        return ''
