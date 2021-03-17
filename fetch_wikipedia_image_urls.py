import sys
import time
from functools import partial

import requests
from bs4 import BeautifulSoup


def fetch_image_url(query):
    response = requests.get(f"https://en.wikipedia.org/w/index.php?title={query}")
    response.raise_for_status()
    html = response.content
    soup = BeautifulSoup(html, features="html5lib")
    image_url = soup.select_one("table.infobox").select_one("img")["src"]
    if not image_url.startswith("http"):
        image_url = "http:" + image_url
    return image_url


if __name__ == "__main__":
    fetch_image_urls(db_file, output_file)
