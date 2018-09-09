
import json
import pprint
from sklearn.datasets import fetch_20newsgroups
from sklearn.decomposition import NMF, LatentDirichletAllocation
from nltk.corpus import brown
from gensim import corpora, models
import gensim
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer

from nltk.corpus import stopwords


if __name__=="__main__":
    json_data = open("reddit_data.json").read()
    # with open('reddit_data.json', 'w+') as outfile:
    #     json.dump(data, outfile, sort_keys=True, indent=4, separators=(',', ': '))
    dic = {}

    stop_words = open('stopword.txt', 'r')
    stop_words = stop_words.readlines()
    stop_words = [x.strip() for x in stop_words]

    tokenizer = RegexpTokenizer(r'\w+')

    p_stemmer = PorterStemmer()

    data = json.loads(json_data)
    for text in data:
        print(text)
        #pprint.pprint(data[text])
        i = 0
        for x in data[text]:
            raw = x.lower()
            tokens = tokenizer.tokenize(raw)
            stopped_tokens = [i for i in tokens if not i in stop_words]
            #pprint.pprint(topped_tokens)

            cleantexts = [p_stemmer.stem(i) for i in stopped_tokens]

            i += 1


    print(dic)
