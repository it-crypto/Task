import pandas as pd
import time



def main():
    start = time.perf_counter()
    inFile = open('/home/web/Desktop/Darkweb/output.csv', 'r')
    outFile = open('/home/web/Desktop/Darkweb/highlight.csv', 'a+')
    listLines = []
    for line in inFile:

        if line in listLines:
            continue

        else:
            outFile.write(line)
            listLines.append(line)

    outFile.close()
    inFile.close()
    finish = time.perf_counter()
    print(f'finished in {round(finish - start, 2)} seconds')

