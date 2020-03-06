Muhammad Luqman@DESKTOP-7MEP61Q MINGW64 ~/test232/api (master)
$ cat wikicrawler.py
#!/usr/bin/env python

import sys
import wikipedia
import requests

from bs4 import BeautifulSoup

from urllib.parse import urljoin

def extract_links(url):

page = wikipedia.page(url)
links = []
for link in links:
        print link["page"]
    for link in page.links:
        links.append({
            "text": link["page"],

            "href": link["page"]
        })
    return links

if _name_ == "_main_":

    if len(sys.argv) != 2:

        print("\nUsage:\n\t{} <URL>\n".format(sys.argv[0]))

        sys.exit(1)

    for link in extract_links(sys.argv[-1]):

        print("[{}]({})".format(link["text"], link["href"]))