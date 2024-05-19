from tbselenium.tbdriver import TorBrowserDriver
import re
import time
import pandas as pd
import concurrent.futures
import requests

def highlight(element):
    #"""Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent
    #def apply_style(s):
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, "color: black; background-color: yellow")




def geturl(source_url):

            driver = TorBrowserDriver("/home/web/Downloads/tor-browser_en-US")
            driver.get(source_url)
            value1 = driver.find_elements_by_xpath("//*[contains(text(),'VISA')]")
            print(value1)
            if value1:
                 for links in value1:
                       highlight(links)
            value2 = driver.find_elements_by_xpath("//*[text()[contains(.,'Visa')]]")
            print(value2)
            if value2:
                for links in value2:
                      highlight(links)
            value3 = driver.find_elements_by_xpath("//h2[text()[contains(.,'Visa')]]")
            print(value3)
            if value3:
              for links in value3:
                   highlight(links)
            value4 = driver.find_elements_by_xpath("//*[text()[contains(.,'Master')]]")
            print(value4)
            if value4:
                 for links in value4:
                    highlight(links)
            value5 = driver.find_elements_by_xpath("//*[contains(text(),'MASTER')]")
            print(value5)
            if value5:
                for links in value5:
                  highlight(links)
            value6 = driver.find_elements_by_xpath("//h2[text()[contains(.,'MASTER')]]")
            print(value6)
            if value6:
              for links in value6:
                   highlight(links)



def main():
    df = pd.read_csv('/home/web/Desktop/Darkweb/highlight.csv', header=None)
    #print(df.head())
    for ind in df.index:
        geturl(df[0][ind])












