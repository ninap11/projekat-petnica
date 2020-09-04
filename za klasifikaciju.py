
txt = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\sites\wsj2.txt", "r", encoding="utf-8")
lines = txt.readlines()
txt.close()

c = 0

# for c in range(len(lines)):
#     line = lines[c]
#     semi = line.find(" ")
#     if semi == -1:
#         print(c)
#     else:
#         lines[c] = line[0:semi+11] + " " + "&" + " " + line[semi+12:] 



for c in range(len(lines)):
    line = lines[c]
    semi = line.find(";")
    if semi == -1:
        print(c)
    else:
        lines[c] = line[0:semi] + "&" + line[semi+1:] 


# for c in range(len(lines)):
#     line = lines[c]
#     lines[c] = "#ws" + str(c) + " " + line

#  lines[c] = "#cd" + str(c) + " " + line


txt = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\sites\wsj3.txt", "w", encoding="utf-8-sig")
txt.writelines(lines)
txt.close()
