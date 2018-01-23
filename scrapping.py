import requests, bs4, lxml, json


def get_location():
    site = "http://freegeoip.net/json/"

    req = requests.get(site)

    retorno = json.loads(req.text)

    codigo_cidade = retorno["region_code"].lower()

    codigo_cidade = codigo_cidade + "eae men"
    print(codigo_cidade)   




if __name__ == "__main__":
    get_location()

# {"key": value, key2:felix, key3:tarcisio}