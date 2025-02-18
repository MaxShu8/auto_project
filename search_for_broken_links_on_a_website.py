from urllib.parse import urljoin
from Settings import *
from bs4 import BeautifulSoup

import requests
import string

SITE = "https://vozovoz.ru/"
visited = ["https://vozovoz.ru/actions/perevezyom_za_250_rubley_po_severo-zapadu/"]

def find_404(url, parent):
    if url in visited:
        return
    else:
        visited.append(url)
    print("url =", url)
    try:
        html = get_html(url)
        soup = BeautifulSoup(html, "html.parser")
        elements = soup.select("a")
        for element in elements:
            if not element.has_attr("href"):
                continue
            href = element["href"]
            if href.startswith(".") or href.startswith("#") or href.startswith(f"{SITE}upload/android/") or href.startswith("tel:+"):
                continue
            for i in string.ascii_lowercase:
                if href.startswith(f"{SITE}order/create/{i}") or href.startswith(f"/order/create/{i}"):
                    return
            href = urljoin(url, href)
            print("href =", href)
            if href.startswith(SITE):
                find_404(href, url)
    except ResourceWarning:
        message = f"🔨 Битая ссылка:\n{url}\nНа странице:\n{parent}"
        print(message)
        send_message_tg(message, token, group_id_predprod)

def get_html(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        raise ResourceWarning()
    return response.text


if __name__ == "__main__":
    find_404(SITE, SITE)


