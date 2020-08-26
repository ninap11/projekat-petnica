import random

txt = open(r'D:\Projekat\New folder\NewsBTC.txt', "r", encoding="utf-8")
ana = open(r'D:\Projekat\New folder\analiza.txt', "a", encoding= "utf-8")
lines = txt.readlines()
# print(lines)
l = len(lines)
# l = 30
c = 0
txt.close()

t19 = [0 for i in range(12)]
t18 = [0 for i in range(12)]
t17 = [0 for i in range(12)]
ts = [t17, t18, t19]

a19 = [[] for i in range(12)]
a18 = [[] for i in range(12)]
a17 = [[] for i in range(12)]
ats = [a17, a18, a19]


a = 0
b = 0
while c < l:
    line = lines[c]
    # print(line[-1])
    try:
        year = int(line[3]) - 7
        month = int(line[5:7])-1
        if year >= 0: 
            ts[year][month] +=1
            ats[year][month].append(line)
        if int(line[3]) == 9:
            a+=1
    except:
        b+=1
        print(c)

    c+=1
o = 0    
# print(ats, ts)

train_set = open(r'D:\Projekat\New folder\train set.txt', "a", encoding= "utf-8")
test_set = open(r'D:\Projekat\New folder\test set.txt', "a", encoding= "utf-8")
train_set.write('\n')
test_set.write('\n')

y = -1
m = -1
for y in range(3):
    year = ts[y]
    print(y)
    for m in range(12):
        month = year[m]
        # print("m", month)
        if month <= 14:
            # print("aaaaaaa")
            counter = 0
            for article in ats[y][m]:
                # print(article, month, counter)
                if counter <= int(month * 0.7):
                    # print("ämmmm")
                    train_set.write(article)
                else:
                    test_set.write(article)
                counter += 1
            # print("c", counter)
        else:
            rs = []
            for i in range(10):
                r = random.randint(0, month-1)
                while r in rs:
                    print(rs, r)
                    r = random.randint(0, month-1)
                rs.append(r)
                print(y, m, r)
                article = ats[y][m][r]
                train_set.write(article)
            for i in range(4):
                r = random.randint(0, month-1)
                while r in rs:
                    r = random.randint(0, month-1)
                rs.append(r)
                article = ats[y][m][r]
                test_set.write(article)
                
                    

                