#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 22:20:31 2022

@author: mingtsung
"""

import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor   

web = requests.get('https://azurlane.koumakan.jp/wiki/List_of_Ships_by_Image', cookies={'over18':'1'})
soup = BeautifulSoup(web.text, "html.parser")
imgs = soup.find_all('img')
name = -6
img_urls = []             
c = 0             
for i in imgs:                       
    if c%2 == 1:
        img_urls.append([i['src'], name])    
        name = name + 1                      
    c+=1
    
def download(url):                     
    print(url)                           
    jpg = requests.get(url[0])           
    if url[1] >= 0:
        f = open(f'pic/azurlane_{url[1]}.jpg', 'wb')   
        f.write(jpg.content)                 
        f.close()

executor = ThreadPoolExecutor()         
with ThreadPoolExecutor() as executor:
    executor.map(download, img_urls) 