import requests


def main():
    cities= ["Лондон", "Череповец", "SVO"]
    params = {"n": "", "M": "", "m": "", "q": "", "T": "", "lang": "ru" }
    url_template = 'https://wttr.in/{}'
    for city in cities:
        url = url_template.format(city)
        response = requests.get(url, params=params)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
