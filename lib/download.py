import requests


def run(url):
    data = requests.get(url)
    return data.text
