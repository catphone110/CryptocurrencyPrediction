import urllib
import re
import ystockquote
import pprint


def main():
    #get_quote('TLSA')
    ##print(ystockquote.get_bid_realtime('GOOGL'))
    import csv
    with open("alldata.csv", 'rb') as oldfile:
        spamreader = csv.reader(oldfile)
        #for row in spamreader:
        print(spamreader)

if __name__=="__main__":
    main()