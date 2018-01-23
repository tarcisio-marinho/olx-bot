import requests, bs4 as bs, lxml, json

"""
no codigo html tem um link que é o next
é um link pra proxima pagina de busca
apos percorrer todas as ofertas de uma pagina, ir para a proxima


ao achar um produto, acessar o seu link de oferta 
pegar dados como -> preco, nome do vendedor, etc
"""

def get_url():
    site = "http://freegeoip.net/json/"
    req = requests.get(site)
    retorno = json.loads(req.text)
    codigo_cidade = retorno["region_code"].lower()  
    codigo_olx = "http://" + codigo_cidade + ".olx.com.br/?q="
    return codigo_olx

def get_content_olx(url_olx, search):
    url_olx = url_olx + search
    req_olx = requests.get(url_olx)
    
    soup = bs.BeautifulSoup(req_olx.text, "lxml")
    
    nomes_e_links = {}
    nomes = []
    
    retorno = soup.find_all("h3")
    for oferta in retorno:
        nova_oferta = oferta.text.replace("\t", "").replace("\n", "")
        if(search in nova_oferta):
            nomes.append(nova_oferta.lower())

    sites = soup.find_all("a")
    for site in sites:
        for nome in nomes:
            try:
                new = site.get("title").lower()
            except AttributeError:
                new = site.get("title")

            if(nome == new):
                nomes_e_links[new] = site.get("href")

    for i in nomes_e_links:
        print(str(i), " >>> ",str(nomes_e_links[i]))


    # link = soup.find_all("link")
    # for l in link:
    #     if("next" in l.get("rel")):
    #         print(l.get("href"))


if __name__ == "__main__":
    url = get_url() 
    search = "ps4"
    get_content_olx(url, search)

