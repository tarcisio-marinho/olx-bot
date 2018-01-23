import requests, bs4, lxml, json


def get_url():
    site = "http://freegeoip.net/json/"
    req = requests.get(site)
    retorno = json.loads(req.text)
    codigo_cidade = retorno["region_code"].lower()  
    codigo_olx = "http://" + codigo_cidade + ".olx.com.br"
    return codigo_olx



if __name__ == "__main__":
    get_url()

# {"key": value, key2:felix, key3:tarcisio}