import requests
import sys

def get_html_requests(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    else:
        print(f"[  {r.status_code}  ] Erreur requets a {url}")
        return r.status_code
    
def main(argc,argv):
    return 0;

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