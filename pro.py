from bs4 import BeautifulSoup
from selenium import webdriver

import time
import csv

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("Z:\app\class127\chromedriver")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers=["V mag","name","bayer","distance","class","mass","radius","luminosity"]
    stardata=[]
    for i in range(0,428):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for trtag in soup.find_all("tr"):
            tdtags=ultag.find_all("td")
            templist=[]
            for index,litag in enumerate(tdtags):
                if index==1:
                    templist.append(tdtag.find_all("a")[0].contents[0])
                else:
                    try:
                        templist.append(tdtag.contents[0])
                    except:
                        templist.append("")
            stardata.append(templist)
        browser.find_element_by_xpath("//*[@id=primary_coloumn]/footer/div/div/div/nav/span[2]/a").click()
    with open("star.csv",'w') as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(stardata)
scrape()
