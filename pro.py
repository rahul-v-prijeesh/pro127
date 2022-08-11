
from bs4 import BeautifulSoup
from selenium import webdriver

import time
import csv

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("Z:\app\class127\chromedriver")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers=["name","distance","mass","radius"]
    stardata=[]
    for i in range(0,428):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for trtag in soup.find_all("tr"):
            tdtags=trtag.find_all("td")
            name=[]
            distance=[]
            mass=[]
            radius=[]
            for index,tdtag in enumerate(tdtags):
                if index==1:
                    name.append(tdtag.contents[0])
                elif index==3:
                     distance.append(tdtag.contents[0])
                elif index==5:
                     mass.append(tdtag.contents[0])
                elif index==6:
                     radius.append(tdtag.contents[0])   
                 
            stardata.append([name,distance,mass,radius])
        #browser.find_element_by_xpath("//*[@id=primary_coloumn]/footer/div/div/div/nav/span[2]/a").click()
    with open("star.csv",'w') as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(stardata)
scrape()

