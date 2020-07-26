import csv
import os.path
csv_dictionary = open(os.path.join("D:\Downloads","LoughranMcDonald_MasterDictionary_2018.csv"), "r", newline="")
reader = csv.reader(csv_dictionary, delimiter=',', quotechar='"')
new_dictionary = open(os.path.join('D:\Projekat','Seconddict.csv'), "w", newline = "")
words = []
negative = []
positive = []
#i = 0
for row in reader:
    words.append(row[0])
#    if i >1:
#        break
#    i += 1
    negative.append(row[7])
    positive.append(row[8])
words.pop(0)
negative.pop(0)
positive.pop(0)
#print(words)

writer = csv.writer(new_dictionary, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
#print(words)
writer.writerow(words)
writer.writerow(negative)
writer.writerow(positive)
print(positive[125])
print("done")
    

    