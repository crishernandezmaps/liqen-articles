#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import time
import os

time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
pre = time[:10] + '-'

def getArticle(url):
    n = url.split('/', 3)
    na = n[-1].replace("/", "")
    name = pre + na + '.md'


    source = 'Source:' + url

    result = requests.get(url)
    c = result.content
    soup = BeautifulSoup(c, "lxml")

    article_text = ''
    article = soup.find("body").findAll('p')
    for element in article:
        article_text += '\n' + ''.join(element.findAll(text = True)) + '\n'

    path = os.path.join('articles', name)

    f = open(path,'w')
    f.write(article_text)
    f.write(source)
    f.close()
    print(article_text)
    return article_text

getArticle(input('Paste your url here: '))
