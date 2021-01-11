#!/usr/bin/env python3

# Python file to download car talk podcast episodes from archive
import argparse
import heapq
import re
from urllib.request import urlopen,urlretrieve
from urllib.parse import urlparse, urlsplit
import os
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup
import errno
import requests
#URL = "https://www.npr.org/podcasts/510208/car-talk"
URL = "https://www.npr.org/podcasts/510208/car-talk/partials?start="
SAVE_DIR = "./test/"
indices = [0,25,49,64,87,110,134,154,180,200,223,247,271]

def save_download_links(urls,save_dir,i):
    num_urls = len(urls)
    for url in urls:
        r = requests.get(url, allow_redirects=True)
        header = r.headers
        content_type = header.get('content-type')
        cd = header.get('content-disposition')
        content = r.content
        fname = save_dir + "best_of_car_talk_" + str(i) + ".mp3"
        with open(fname,'wb') as f:
            f.write(content)
        i = i + 1


    return None

# get all the direct links to episodes
def get_download_links(url):
    dl_links = list()
    #connect to the url
    website = urlopen(url)
    #get the html code
    html = website.read()
    soup = BeautifulSoup(html,features="html.parser")
    # find all the links 
    links = soup.findAll(href=re.compile(r"https://play.podtrac.com/.*",re.IGNORECASE))

    for l in links:
        dl_links.append(l.attrs['href'])

    return dl_links

def main():
    for i in indices:
        url = URL + str(i)
        download_links = get_download_links(url)
        save_download_links(download_links,SAVE_DIR,i)


if __name__=='__main__':
    main()