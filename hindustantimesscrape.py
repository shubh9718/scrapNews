import requests 
import csv
import pandas as pd
from bs4 import BeautifulSoup 

def hindustannews():
    #saving the url
    url='https://www.hindustantimes.com/latest-news'

    #getting the url through requests module
    webResponse = requests.get(url) 

    #check if the server successfully answered the request
    #200 is the HTTP status code for a successful response
    if webResponse.status_code==200:
        
        #extract data from everything(text) on the page
        soup = BeautifulSoup(webResponse.text,'html.parser')

        #find elements with <ul> tag and classs="latest-news-bx"
        nlist = soup.find("ul",{"class":"latest-news-bx"}) 

        #create a csv file if not already exists named "News.csv"
        with open("News.csv",'w',encoding="utf-8") as nfle:
            writer = csv.writer(nfle, dialect='excel')

            #iterate data over the rows with headers 'News and 'Link'
            writer.writerow(['News','Link'])

            #find all tags with 'a' like anchor tag for example
            for news in nlist.findAll("a"):

               #ignore if the text starts with read more
                if news.text.startswith(" read more") or news.text.startswith("read more") :
                    pass
                
                #else print the news
                else:
                    print(news.text)
                    row = news
                    #write the row in file
                    writer.writerow(row)
        #close the file
        nfle.close()
        
        #read the file
        df = pd.read_csv('News.csv')
        df.drop('Link', axis = 1, inplace = True)
        df.to_csv('News.csv', index = False)
        
    #if request is not granted by server print error message
    else: 
        print("Webpage Error") 
        
hindustannews()
