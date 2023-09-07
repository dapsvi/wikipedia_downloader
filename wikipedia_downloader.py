import bs4 as bs
import requests
import os

max_n = 100

base_url = "https://fr.wikipedia.org/wiki/Biologie"

def get_text(url):
    html = requests.get(url).text

    soup = bs.BeautifulSoup(html, "html.parser")
    txt = soup.get_text()
    return txt

def get_links(url):
    html = requests.get(url).text

    soup = bs.BeautifulSoup(html, "html.parser")

    a = soup.find_all("a")

    links = []
    for l in a:
        link = l.get("href")
        if type(link) == str:
            if (link[:6] == "/wiki/") and ("edit" not in link):
                links.append("https://fr.wikipedia.org" + link)
    return links

def add_page_content(url):
    txt = get_text(url)
    with open(os.curdir + "data.txt", "a", encoding="utf-8") as data:
        data.write("\n")
        data.write(txt)

def clear_data():
    with open(os.curdir + "data.txt", "w", encoding="utf-8") as data:
        data.write("")

if __name__ == "__main__":
    # clear_data()
    n=0
    for link in get_links(base_url):
        if n <= max_n:
            add_page_content(link)
            n += 1










        