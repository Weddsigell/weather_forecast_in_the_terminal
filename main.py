import requests


def main():
    city = "Пермь"
    url_template = 'https://wttr.in/{}?nMmqT&lang=ru'
    url = url_template.format(city)
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)


if __name__ == '__main__':
    main()
