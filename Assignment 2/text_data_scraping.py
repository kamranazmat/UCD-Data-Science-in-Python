#!/usr/bin/python
# Kamran Azmat

import requests
from bs4 import BeautifulSoup

# URL to extract: http://mlg.ucd.ie/modules/COMP41680/news/index.html
BASE_URL = "http://mlg.ucd.ie/modules/COMP41680/news/"
PATH = "articles/"

def create_file(filename, article_html):
    filename = PATH + filename.rstrip(".html") + ".txt"
    # open file with write privilege
    f = open(filename, "w")

    for link in article_html.find_all("p", attrs={'class': None}):
        text = link.get_text()
        # skip blank <p> tags and write to the file
        if text != "":
            f.write(text)
    # close the filename
    f.close()

def get_html(url):
    page = requests.get(url)
    html_doc = page.text
    return BeautifulSoup(html_doc, 'html.parser')

def article_scrapping(article_link):
    html = get_html(BASE_URL + article_link)
    create_file(article_link, html)

def web_scraping(extension, filter):
    links = []
    html = get_html(BASE_URL + extension)
    for link in html.find_all("a"):
        link_href = link.get("href")
        if link_href.startswith(filter):
            links.append(link_href)
    return links

def main():
    links = web_scraping("index.html", "month")

    # Web scraping for each month
    for link in links:
        article_links = web_scraping(link, "article")
        for article_link in article_links:
            article_scrapping(article_link)

if __name__ == "__main__":
    main()
