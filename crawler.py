# Import libraries
from urllib.parse import urljoin
from tbselenium.tbdriver import TorBrowserDriver
from bs4 import BeautifulSoup
import os
import concurrent.futures
from urllib.parse import urlparse
import time
import pandas as pd
import csv

path = r'/home/web/Desktop/Darkweb'




# Set for storing urls with same domain
links_intern= set()

# Set for storing urls with different domain
links_extern = set()


# Method for crawling a url at next level
def level_crawler(input_url):
    temp_urls = set()
    current_url_domain = urlparse(input_url).netloc
    results =set()

    driver = TorBrowserDriver("/home/web/Downloads/tor-browser_en-US")
    driver.get(input_url)
    html = driver.page_source
    # Creates beautiful soup object to extract html tags
    beautiful_soup_object = BeautifulSoup(html,"html.parser")

    # Access all anchor tags from input
    # url page and divide them into internal
    # and external categories
    for anchor in beautiful_soup_object.findAll("a"):
        href = anchor.attrs.get("href")
        if (href != "" or href != None or (not href.startswith("#"))):
            href = urljoin(input_url, href)
            href_parsed = urlparse(href)
            href = href_parsed.scheme
            href += "://"
            href += href_parsed.netloc
            href += href_parsed.path
            final_parsed_href = urlparse(href)
            is_valid = bool(final_parsed_href.scheme) and bool(final_parsed_href.netloc)
            if is_valid:
                if current_url_domain not in href and href not in links_extern:
                    print("Extern - {}".format(href))
                    links_extern.add(href)
                    results.add(href)
                if current_url_domain in href and href not in links_intern:
                    print("Intern - {}".format(href))
                    links_intern.add(href)
                    results.add(href)

                    temp_urls.add(href)
    driver.quit()
    output(results)
    return temp_urls


def output(results):
    with open(os.path.join(path, 'crawled_pages.csv'), 'a+', newline='') as file:
        write = csv.writer(file)
        for out in results:
            write.writerow([out])



    # We have used a BFS approach considering the structure as a tree. It uses a queue based approach to traverse links upto a particular depth.

def crawl(input,depth):
    queue = []
    queue.append(input)
    for j in range(depth):
        for count in range(len(queue)):
            url = queue.pop(0)
            urls = level_crawler(url)
            for i in urls:
                queue.append(i)


def main():
    start = time.perf_counter()

    df = pd.read_csv('url.csv', header=None)
    for ind in df.index:
        print(df[0][ind])

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for t in df.index:
            ind = df[0][t]
            data = {executor.submit(crawl, ind, 2)}

    finish = time.perf_counter()

    print(f'finished in {round(finish - start, 2)} seconds')