import requests
import sys
from bs4 import BeautifulSoup

def ft_write(soup: BeautifulSoup, filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

def get_html_requests(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r
    else:
        print(f"[  {r.status_code}  ] Erreur requets a {url}")
        return r.status_code

def link_update_css(soup , dommain):
    for i in soup.find_all("link"):
        i["href"] =  dommain+i["href"]
    return soup

def link_update_img(soup , dommain):
    for a in soup.find_all("img"):
        a["src"] = dommain + a["src"]
    return soup

def link_update_a(soup , dommain):
    for a in soup.find_all("a"):
        a["href"] = dommain + a["href"]
    return soup

def main(argc,argv):
    #url = input("Rentre une url cible : ")
    url = "https://preprod.sagesfemmesdemaia.fr/login#login"
    dommain = "https://preprod.sagesfemmesdemaia.fr"

    soup =  BeautifulSoup(get_html_requests(url).text,"lxml")

    soup = link_update_css(soup,dommain) #mes a jour les liens css
    soup = link_update_img(soup,dommain) #mes a jour les liens img
    soup = link_update_a(soup,dommain) #mes a jour les liens a

    ft_write(soup,"index.html")

if __name__ == '__main__':
    print('''      
 ██████╗██╗   ██╗██████╗ ███████╗██████╗ ██████╗  █████╗ ██╗████████╗
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██║╚══██╔══╝
██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝██████╔╝███████║██║   ██║   
██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██╔══██╗██╔══██║██║   ██║   
╚██████╗   ██║   ██████╔╝███████╗██║  ██║██████╔╝██║  ██║██║   ██║   
 ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝                                                           
    ''')
    main(len(sys.argv),sys.argv) 