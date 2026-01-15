import requests
from bs4 import BeautifulSoup

def scrape(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")

    data=[]

    # Only syllabus section can be gotten theres 
    for h in soup.find_all(["h2","h3"]):
        data.append(h.text.strip())

    for p in soup.find_all("p"):
        text=p.text.strip()
        if len(text)>30:
            data.append(text)

    return list(set(data))
