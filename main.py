import requests


def proxycek(url):
    proxies = []
    response = requests.get(url)

    if response.status_code == 200:
        lines = response.text.split('\n')

        for line in lines:
            if ":" in line:
                proxies.append(line.strip())

    return proxies


def proxykaydet(proxies, filename):
    with open(filename, 'w') as file:
        for proxy in proxies:
            file.write(proxy + '\n')


def main():
    url = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all&simplified=true'
    proxies = proxycek(url)

    proxykaydet(proxies, 'proxies.txt')
    print("Proxies.txt dosyasına kaydedildi")


if __name__ == "__main__":
    main()