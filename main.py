import requests
import sys
from bs4 import BeautifulSoup

def ft_write(soup: BeautifulSoup, filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

def get_html_requests(url):
    r = requests.get(url)

    if r.status_code == 200:
        print(f"[  {r.status_code}  ] requests succsses a {url}")
        return r
    else:
        print(f"[  {r.status_code}  ] Erreur requets a {url}")
        return r

def ping(url):
    r = requests.get(url)
    return r.status_code

def link_update_css(soup, dommain):
    for i in soup.find_all("link"):
        #print(ping(dommain+i.get("href")))
        href = i.get('href')
        if href != None:
            if ping(dommain+href) == 200:
                i['href']= dommain+i["href"]
            
            #.... autre possibiliter
    return soup

def link_update_img(soup,dommain):
    for i in soup.find_all("img"):
        #print(ping(dommain+i.get("href")))
        href = i.get('src')
        if href != None:
            i['src']= dommain+i["src"]
    return soup


def main(argc,argv):
    #url = input("Rentre une url cible : ")
    url = "https://fr.wikipedia.org/w/index.php?returnto=Login+%28informatique%29&title=Sp%C3%A9cial:Connexion&centralAuthAutologinTried=1&centralAuthError=Not+centrally+logged+in"
    dommain = "https://fr.wikipedia.org/"

    soup =  BeautifulSoup(get_html_requests(url).text,"lxml")
    soup = link_update_css(soup,dommain) #mes a jour les liens css
    soup = link_update_img(soup,dommain) #mes a jour les liens img
    ft_write(soup,"index.html")

if __name__ == '__main__':
    main(len(sys.argv),sys.argv) 