import csv
import pickle
import nltk

csvfile = open(r'C:\Users\Bratislav\Desktop\petnica projekat\data\csv\Seconddict.csv', newline = '')
reader = csv.reader(csvfile)

words = reader.__next__()
negative_row = reader.__next__() #strings
positive_row = reader.__next__()


# print(words.index("DEPLORABLE"), negative_row[words.index("DEPLORABLE")], positive_row[words.index("DEPLORABLE")])
## # ##
### ###
## # ##


print(words[0])
vocabulary = set(words)
negative = {word : False for word in words}
# print(negative)
positive = {word : False for word in words}
objective = {word : False for word in words}
all_words = {word : False for word in words}

# print(len(negative))
featureset = []
# classifier_txt = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\featureset.txt", "rb")
# featureset = pickle.load(classifier_txt)
# classifier_txt.close()

for i in range(len(words)):
    # print(i)
    if int(negative_row[i]) != 0:
        # print("haha")
        # print(int(negative_row[i]))
        negative[words[i]] = True
        # dicti = all_words
        # dicti[words[i]] = True
        # tup = (dicti, "n")
        # featureset.append(tup)
        # featureset.append(tup)
    elif int(positive_row[i]) != 0:
        # print("p")
        # print(int(positive_row[i]))
        # print(words[i], "p")
        # dicti = all_words
        # dicti[words[i]] = True
        # tup = (dicti, "p")
        # featureset.append(tup)
        positive[words[i]] = True
    else:
        # print(int(objective_row))
        # print("o")
        # print(words[i], "o")
        objective[words[i]] = True
        # dicti = all_words
        # dicti[words[i]] = True
        # tup = (dicti, "o")
        # featureset.append(tup)

print(negative["ABANDON"])

pos_tuple = (positive, "p")
neg_tuple = (negative, "n")
obj_tuple = (objective, "o")

featureset.append(pos_tuple)
featureset.append(neg_tuple)
featureset.append(obj_tuple)

# address = open(r'C:\Users\Bratislav\Desktop\petnica projekat\data\dictionary featureset.txt', "wb")
# pickle.dump(featureset, address)

classifier = nltk.NaiveBayesClassifier.train(featureset)
print(classifier.classify_many([{"TREE" : True, "BAD": True, "ABANDON":True}, {"A": True}]))

# classifier_txt = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\classifier dicti.txt", "wb")
# pickle.dump(classifier, classifier_txt)
# classifier_txt.close()

# classifier_txt = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\classifier comb.txt", "wb")
# pickle.dump(classifier, classifier_txt)


# featureset_txt = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\feaaa.txt", "rb")

# feature_set = pickle.load(featureset_txt)
# featureset_txt.close()

# new_set = []
# for f in feature_set:
#     print(classifier.classify(f[0]))




# feat = feature_set[0][0]

# print(nltk.classify.accuracy(classifier, feature_set))


# pbdist = open(r'C:\Users\Bratislav\Desktop\petnica projekat\data\pbdist.txt', "w")
# pbdist.write(str(classifier._feature_probdist))
# pbdist.close()


# print(classifier._feature_probdist)

# print(classifier.show_most_informative_features(100))

# pbdist2 = open(r'C:\Users\Bratislav\Desktop\petnica projekat\data\pbdist2.txt', "w")
# pbdist2.write(str(classifier.most_informative_features(100000)))
# pbdist2.close()



# for i in range(len(positive_row)):
#     elem = int(positive_row[i])
#     if elem != 0:  prob_classify(feat).samples()
#         positive.append(elem)
#     else:
#         objective.append(elem)

# obj_dict = {word: (word in objective) for word in vocabulary}
# print(obj_dict["AARDVARK"])


# print(words[0])

# for row in reader:
    
    
# print(test)
