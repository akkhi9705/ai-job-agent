import requests
from bs4 import BeautifulSoup

def extract_jd(url):

    response = requests.get(url)

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    return soup.get_text(
        separator=" ",
        strip=True
    )