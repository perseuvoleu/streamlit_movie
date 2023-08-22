from bs4 import BeautifulSoup
import requests
import re


class Serial:
    def __init__(self, link, title, img):
        self.link = link
        self.title = title
        self.img = img
        self.videos = []

    def scrape_video(self):
        response = requests.get(
            url=self.link,
        )

        soup = BeautifulSoup(response.text, "html.parser")

        links = soup.find_all("a")

        pattern = re.compile(r"https://(ok\.ru)/")

        for link in links:
            url = link.get("href")

            if pattern.match(url):
                self.videos.append(url)


def scrape_seriale():
    pagini = 3
    lista_seriale = []
    for pagina in range(1, pagini):
        url = "https://blogul-lui-atanase.ro/categorie/seriale-coreene-2023/page/{}/".format(
            str(pagina)
        )
        page = requests.get(url)
        if page.status_code == 200:
            # print("Status 200")
            soup = BeautifulSoup(page.content, "html.parser")

            # Găsiți și eliminați toate tag-urile <noscript>

            for article in soup.find_all("article"):
                element = article.find("h2", class_="entry-title")
                title = element.text
                link = element.a["href"]
                img = article.find(attrs={"data-src": True})["data-src"]
                s = Serial(link, title, img)
                lista_seriale.append(s)
    return lista_seriale


# if __name__ == "__main__":
#     scrape_seriale()
