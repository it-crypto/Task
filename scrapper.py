from bs4 import BeautifulSoup
from tbselenium.tbdriver import TorBrowserDriver
import re
import os
from urllib.parse import urljoin
import concurrent.futures
import time
import csv
import pandas as pd


path = r'/home/web/Desktop/Darkweb'


def get_keywords(base,keywords):
    driver = TorBrowserDriver("/home/web/Downloads/tor-browser_en-US")
    driver.get(base)
    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")
    results = set()
    for names in keywords:
        names = re.compile(names,re.IGNORECASE)
        for link in soup.find_all('a',string=names):
            str  = link.get('href')
            if not str.startswith('#'):
                if not str.startswith('mailto'):
                    data = urljoin(base,str)
                    results.add(data)

    driver.quit()
    output(results)


# writing the data into the  csv file
def output(results):
    with open(os.path.join(path, 'output.csv'), 'a+', newline='') as file:
        write = csv.writer(file)
        for out in results:
            write.writerow([out])



keywords = ['VISA','Master','Paypal','Cards']



def main():
    start = time.perf_counter()
    df = pd.read_csv('crawled_pages.csv', header=None)
    print(df.head())
    # by this statement we are suing differnt threads to execute different files concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # data = {executor.submit(get_keywords,base,keywords): base for base in f1}  # in submit method we are calling get_keywords and giving base,keywords as arguments whereas base is in loop
        # because base have to read every file in 1.txt
        for t in df.index:
            base = df[0][t]
            data = {executor.submit(get_keywords, base, keywords)}

    finish = time.perf_counter()

    print(f'finished in {round(finish - start, 2)} seconds')



