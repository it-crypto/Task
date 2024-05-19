import crawler
import scrapper
import duplicate
import highlight
import time


print("crawler module start")
crawler.main()
time.sleep(300)
print("crawler module finished")
print("scrapper module start")
scrapper.main()
time.sleep(120)
print("scrapper module finished")
print("Duplicate removal start")
duplicate.main()
time.sleep(100)
print("Duplicate removal finished")
print("highlight the keywords")
highlight.main()
print("finished")

