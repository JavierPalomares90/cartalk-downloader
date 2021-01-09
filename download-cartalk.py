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
URL = "https://www.npr.org/podcasts/510208/car-talk"
SAVE_DIR = ""

def save_download_links(urls,save_dir):
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

    return dl_links

def main():
    download_links = get_download_links(URL)

    save_download_links(download_links,SAVE_DIR)


if __name__=='__main__':
    main()