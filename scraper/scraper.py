from itertools import count
from turtle import title
from unittest import result
from attr import attr
import requests
from bs4 import BeautifulSoup


class Webscraper:
    '''
    Scrape a Wikipedia page and record which passages need citations
    '''
    def __init__(self):
        self.url = "https://en.wikipedia.org/wiki/History_of_Mexico"
        self.anchorList = []
        self.passeges = []
    
    def get_citations_needed_count(self):
        '''
        methods which giting a URL for a wikipedia pge and then return  the number of Citintion needed 
        '''
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, "html.parser")
        results_div = soup.find("div", id="mw-content-text")
        paragraph_list = results_div.find_all("p")
        count = 0
        for i in paragraph_list:
            anchors = i.find_all("a")
            for a in anchors:
                anc = a.attrs
                if anc.get("title") == "Wikipedia:Citation needed" :
                    self.anchorList.append(anc)
                    self.passeges.append(i.get_text())
        return len(self.anchorList)


    def get_citations_needed_report(self):
        '''
        method for printing  all passeges need citation 
        '''
        resultpass = ""
        if self.get_citations_needed_count() == 0 :
            resultpass = "No Citation is there !"
        else:
            for i in range(len(self.anchorList)):
                resultpass+= (f'''Citation needed for :{self.passeges[i]}\n''')
        return resultpass