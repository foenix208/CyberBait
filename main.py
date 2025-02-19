import requests
import sys
from bs4 import BeautifulSoup

def ft_write(soup: BeautifulSoup, filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

def get_html_requests(url):
    r = requests.get(url)
    if r.status_code == 200:
        print(f"[  {r.status_code}  ] Erreur succsses a {url}")
        return r
    else:
        print(f"[  {r.status_code}  ] Erreur requets a {url}")
        return r

def ping(url):
    r = requests.get(url)
    return r.status_code

def link_update_css(soup, dommain):
    for i in soup.find_all("link"):
        href = i.get('href')
        
        if href != None:
            if ping(dommain+href) == 200:
                i['href']= dommain+i["href"]
            #....

    return soup

def main(argc,argv):
    #url = input("Rentre une url cible : ")
    url = "https://www.celignis.com/output/login.php"
    dommain = "https://www.celignis.com/output/"

    soup =  BeautifulSoup(get_html_requests(url).text,"lxml")
    soup = link_update_css(soup,dommain) #mes a jour les liens css
    ft_write(soup,"index.html")

if __name__ == '__main__':
    main(len(sys.argv),sys.argv) 