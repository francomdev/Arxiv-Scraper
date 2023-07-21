import requests 
from bs4 import BeautifulSoup
from datetime import date


topic = "quant-ph"
KEYWORDS = ["thermodynamics ", "engine ", "heat ", "battery ", "batteries ", "machines ", "measurement "]


URL = "https://arxiv.org/list/"+topic+"/new"
req = requests.get(URL)
soup = BeautifulSoup(req.text, 'html.parser')

titles = soup.find_all(class_="list-title")
authors = soup.find_all(class_ = "list-authors")
abstracts = soup.find_all("p", class_= "mathjax")

num_papers = len(abstracts)

today = date.today()

with open("Arxiv_" + str(today) + ".txt", 'w') as f:
    for i in range(num_papers):
        for word in KEYWORDS:
            if word in titles[i].text:
                f.write(titles[i].text)
                f.write(authors[i].text)
                f.write(abstracts[i].text)
            elif word in abstracts[i].text:
                f.write(titles[i].text)
                f.write(authors[i].text)
                f.write(abstracts[i].text)


