
import os.path
import nltk 
from nltk import sentiment
from nltk.sentiment import util
from nltk.corpus import stopwords
nltk.download('punkt')
import csv
from nltk import classify
from nltk.classify import naivebayes



txt_file2 = open(os.path.join("D:\Projekat", "a.txt"), "r+")
separated_file = [nltk.word_tokenize(t) for t in nltk.sent_tokenize(txt_file2.readlines()[0])]

values = ["neu", "neu"]
# for sentence in separated_file:
#    print(sentence)
#    value = input() #pos or neg value of the sentence
#    values.append(value)


no_stop_words = []
vocabulary = set()


for sentence in separated_file:
    no_stop_sentence = [word.upper() for word in sentence if not word in nltk.corpus.stopwords.words('english')]
    no_stop_words.append(no_stop_sentence)
    vocabulary.update(no_stop_sentence)

nltk.sentiment.util.mark_negation(no_stop_words, False, True)

c = 0
featureset = []
print(no_stop_words)



for sentence in no_stop_words:
    d = {word: (word in sentence) for word in vocabulary}
    tup = (d, values[c])
    featureset.append(tup)
    c += 1

print(featureset)

classifier = nltk.NaiveBayesClassifier.train(featureset)
print(classifier.show_most_informative_features(10))
print(featureset)
print(vocabulary)

print("done")