import requests
from bs4 import BeautifulSoup

def getPDFs(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    initial_uris = []
    final_uris = []
    byte_size = []
    for link in soup.find_all('a'):
        r = requests.get(link.get('href')).headers
        if r['Content-Type'] == 'application/pdf':
            initial_uris.append(link.get('href'))
            final_uris.append(requests.get(link.get('href')).url)
            byte_size.append(r['Content-Length'])
            print(list(zip(initial_uris,final_uris,byte_size)))

if __name__ == '__main__':
    getPDFs(input('What is your url'))