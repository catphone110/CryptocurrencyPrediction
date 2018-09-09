import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

reddit_data = None
with open('reddit_data.json') as f:
    reddit_data = json.load(f)

def remove_stopword(reddit_data):
    nltk.download()
    cleaned_data = {}
    stop_word = open('stopword.txt', 'r')
    stop_word = stop_word.readlines()
    stop_word = [x.strip() for x in stop_word]
    p_stemmer = PorterStemmer()

    for date in reddit_data:
        date_word_data = []
        for sentence in reddit_data[date]:
            word_tokens = word_tokenize(sentence)
            for word in word_tokens:
                if word.lower() not in stop_word:

                    date_word_data.append(word.lower())

        date_word_data = [p_stemmer.stem(i) for i in date_word_data]
        cleaned_data[date] = date_word_data
    return cleaned_data
    # with open('cleaned_reddit_data.json', 'w') as outfile:
    #     json.dump(cleaned_data, outfile, sort_keys=True, indent=4, separators=(',', ': '))

def main():
    remove_stopword(reddit_data)


if __name__ == '__main__':
    main()