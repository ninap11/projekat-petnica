
import nltk.corpus
import nltk
import nltk.stem
nltk.download("sentiwordnet")
nltk.download("averaged_perceptron_tagger")
from nltk.corpus import sentiwordnet as swn
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer


# from taggers import WordNetTagger

def tag_func(tag):
    if tag[0] == "N":
        tag = "n"
        return tag
    if tag[0] == "J":
        tag = "a"
        return tag
    if tag[0] == "V":
        tag = "n"
        return tag
    if tag[0] == "R":
        tag = "r"
        return tag


def no_stopwords_func(article):
    no_stops_article = [word for word in article if not word.lower() in corpus]
    return no_stops_article

def tfidf(article, articles):



txt_file = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\train set.txt", "r+", encoding= "utf-8-sig")
article = txt_file.readlines()[7]
article = article[article.find(" ")+11:]

tokenizer = RegexpTokenizer(r'\w+')
corpus = nltk.corpus.stopwords.words('english')
stemmer = PorterStemmer()

sentences = nltk.sent_tokenize(article)
# print(words)
lemmatizer = WordNetLemmatizer()
# tagger = WordNetTagger()

syns = []
no_lemmas = []
lemmas = []
a = 0
b = 0
c = 0

pos = 0
neg = 0
obj = 0

for sentence in sentences:
    # print(sentence)
    pos1, neg1, obj1 = 0, 0, 0
    syns = []
    words = tokenizer.tokenize(sentence)
    no_stop = no_stopwords_func(words)
    # print(no_stop)
    
    # print(ws)
    tokens = nltk.pos_tag(no_stop)
    # print(token)
    for token in tokens:
        lemma = lemmatizer.lemmatize(token[0])
        stem = stemmer.stem(lemma)
        stemmed        
        
    

#     if obj1 == max(pos1, neg1, obj1):
#         print("a")
#         if obj1 == pos1:
#             pos += 1
#             print("p")
#         elif obj1 == neg1:
#             neg += 1
#             print("n")
#         else:
#             obj += 1
#     elif pos1 == max(pos1, neg1, obj1):
#         print("b")    
#         if pos1 == neg1:
#             obj += 1
#             print("o")
#         else:
#             pos +=1
#     elif neg1 == max(pos1, neg1, obj1):
#         print("c")
#         if neg1 == pos1:
#             obj += 1
#             print("o")
#         else:
#             neg += 1
#             print("n")

# print(pos, neg, obj)



# for synset in syns:
#     pos, neg, obj = 0, 0, 0
#     pos += synset.pos_score()
#     neg += synset.neg_score()
#     obj += synset.obj_score()
#     print(obj, pos, neg)
# print(pos, neg, obj)
# # print(syns)
# print(no_lemmas)
# print(a, b, c)
# # print(swn.senti_synset("Bad.n.01"))