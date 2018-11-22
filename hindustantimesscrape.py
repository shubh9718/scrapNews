import requests 
import csv
import pandas as pd

from bs4 import BeautifulSoup 

def htnews(): 
    url1='https://www.hindustantimes.com/latest-news'
    # url2='https://www.hindustantimes.com/top-news'
    
    web_response = requests.get(url1) 
    
