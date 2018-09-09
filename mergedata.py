import json
import csv

def merge_data(price_data, sentiment_data):
    date_iter = datetime.date(2018, 5, 1)
    myData = [['Date', 'Price', 'Sentiment']]
    myFile = open('merged_data.csv', 'w+')
    with myFile:
        writer = csv.writer(myFile)
        for i in range(len(price_data)):
            str_date = str(date_iter).replace("-", "")
            date_iter -= datetime.timedelta(days=1)
            #writer.writerow([str(date_iter), price_data[str(date_iter)], sentiment_data[str(date_iter)]])



if __name__ =="__main__":
    bitcoin_price={}
    with open('bitcoin_price.json') as f:
        bitcoin_price = json.load(f)
    sentiment_score={}
    with open('sentiment_score.json') as f:
        sentiment_score = json.load(f)
    merge_data(bitcoin_price,sentiment_score)