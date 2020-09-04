import random

# txt = open(r'C:\Users\Bratislav\Desktop\petnica projekat\data\objectives.txt', "r", encoding="utf-8")
# lines = txt.readlines()
# print(len(lines))
# lines = [1 for i in range(1300)]
# fixed = []

# values_file = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\values test set.txt", "r+", encoding= "utf-8")
# values = values_file.readlines()

# ts_txt= open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\train set.txt", "r", encoding= "utf-8")
# lines = ts_txt.readlines()
# vts_txt = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\values.txt", "r", encoding= "utf-8")
# values = vts_txt.readlines()



# ts_txt.close()
# vts_txt.close()

# plines = []
# pvalues = []
# olines = []
# ovalues = []
# i = 0

# while i < len(lines):
#     print(i)
#     line = lines[i]
#     value = values[i][values[i].find(" ")+1:].strip()
#     print("v", [value])
#     idnum = values[i][:values[i].find(" ")].strip()
#     if value == "p" or value == "n":
#         plines.append(line)
#         full = idnum + " " + value + "\n"
#         pvalues.append(full)
        
#     else:
#         olines.append(line)
#         full = idnum + " " + value + "\n"
#         ovalues.append(full)
#     i += 1    


p_txt= open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\p and n.txt", "r", encoding= "utf-8")
plines = p_txt.readlines()
p_values = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\p and n values.txt", "r", encoding= "utf-8")
pvalues = p_values.readlines()

new_txt= open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\new trainset.txt", "r", encoding= "utf-8")
lines = new_txt.readlines()

new_values = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\new traintset values.txt", "r", encoding= "utf-8")
values = new_values.readlines()

# o_txt= open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\obj.txt", "r", encoding= "utf-8")
# lines = o_txt.readlines()
# o_values = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\obj values.txt", "r", encoding= "utf-8")
# values = o_values.readlines()
p_txt.close()
p_values.close()
new_txt.close()
new_values.close()

for i in plines:
    lines.append(i)
for j in pvalues:
    values.append(j)
    



# for i in plines:
#     lines.append(i)

# for i in pvalues:
#     values.append(i)

# for i in olines:
#     lines.append(i)

# for i in ovalues:
#     values.append(i)

# print(values)



# ts_txt.close()
# vts_txt.close()

# s = len(lines)
# print(s)
# for i in range(500):
#     r = random.randint(0, s-1)
#     print(r, s)
#     del lines[r]
#     del values[r]
#     s -= 1




new_txt= open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\new trainset.txt", "w", encoding= "utf-8")
new_txt.writelines(lines)

new_values = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\new traintset values.txt", "w", encoding= "utf-8")
new_values.writelines(values)

new_txt.close()
new_values.close()
# values = []

# for l in lines:
#     idnum = l[:l.find(" ")].strip()
#     full = idnum + " " + "o" + "\n"
#     values.append(full)

# newlines = []
# newvalues = []

# i = 0

# while i < len(lines):
#     print(i)
#     line = lines[i]
#     value = values[i][values[i].find(" ")+1:].strip()
#     idnum = values[i][:values[i].find(" ")].strip()
#     if value == "p" or value == "n":
#         newlines.append(line)
#         full = idnum + " " + value + "\n"
#         newvalues.append(full)
#         print(i)
#     i += 1    



# new_txt= open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\p and n.txt", "w", encoding= "utf-8")
# new_txt.writelines(newlines)

# new_values = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\p and n values.txt", "w", encoding= "utf-8")
# new_values.writelines(newvalues)

# vts_txt.writelines(values)

# new_txt.close()
# new_values.close()

os = 0
ps = 0
ns = 0

i = 0
o = 0
c = 0

# txt.close()
# values_file.close()

# while i < len(lines):
#     # title = lines[i][lines[i].find(" ")+1:].strip()
#     value = values[i][values[i].find(" ")+1:].strip()

#     if value == "o":
#         os +=1
#     if value == "n":
#         ns +=1
#     if value == "p":
#         ps +=1
#     i+=1
# print(os, ps, ns)    
    # print(value)
    # idnum = values[i][:values[i].find(" ")].strip()
    # ind = lines[i].find(" ")
    # semi = lines[i].find(";")
    # title = lines[i][ind+12: semi].strip()

    


# while i < len(lines):
#     # title = lines[i][lines[i].find(" ")+1:].strip()
#     value = values[i][values[i].find(" ")+1:].strip()

#     # print(value)
#     idnum = values[i][:values[i].find(" ")].strip()
#     # ind = lines[i].find(" ")
#     # semi = lines[i].find(";")
#     # title = lines[i][ind+12: semi].strip()

#     if value == "o":
#         newlines.append(lines[i])
#         full = idnum + " "+"o" + "\n"
#         newvalues.append(full)
#     i+=1


# new_txt= open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\objektivni.txt", "w", encoding= "utf-8")
# new_txt.writelines(newlines)

# new_values = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\objektivni values.txt", "w", encoding= "utf-8")
# new_values.writelines(newvalues)


# while c < len(lines):
#     line = lines[c]
#     if len(line) > 30:
#         ind = line.find(" ")
#         # print("l",line[ind+10])
#         if line[ind+12] == ";":
#             lines[c] = line[:ind+12] + line[ind+13:]
#             # print(lines[c][0:30])
#     c+=1

        
# writ.writelines(lines)
# writ.close()


# txt = open(r'C:\Users\Bratislav\Desktop\petnica projekat\data\test set 300.txt', "w", encoding="utf-8")
# values_file = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\values test 300.txt", "w", encoding= "utf-8")
# txt.writelines(lines)
# values_file.writelines(values)


# objectives = []


# txt.close()
# values_file.close()


# writ = open(r'C:\Users\Bratislav\Desktop\petnica projekat\data\objectives.txt', "r", encoding="utf-8")
# lines = writ.readlines()
# c = 0
# writ.close()

# reader = open(r'C:\Users\Bratislav\Desktop\petnica projekat\data\deleted.txt', "r", encoding="utf-8")
# lines = reader.readlines()

# txt = open(r'C:\Users\Bratislav\Desktop\petnica projekat\data\values.txt', "r", encoding="utf-8")
# tlines = txt.readlines()

# reader.close()
# txt.close()

# i = 0
# found = False
# while i < len(lines):
#     # title = lines[i][lines[i].find(" ")+1:].strip()
#     idnum = lines[i][:lines[i].find(" ")].strip()
#     for t in tlines:
#         if idnum in t:
#             found = True
#     if found:
#         del tlines[i]
#         del lines[i]
#     else:
#         i+=1
    

#     # i+=1

# reader = open(r'C:\Users\Bratislav\Desktop\petnica projekat\data\deleted.txt', "w", encoding="utf-8")
# reader.writelines(lines)

# txt = open(r'C:\Users\Bratislav\Desktop\petnica projekat\data\values fixed.txt', "w", encoding="utf-8")
# txt.writelines(tlines)

# reader.close()
# txt.close()


        # ind = lines[i].find(" ")
        # semi = lines[i].find(";")
        # title = lines[i][ind+13: semi]
        # full = idnum + " " + title + "\n"
        # writ.write(full)

# writ.close()

# txt = open(r'C:\Users\Bratislav\Desktop\petnica projekat\data\train 1000.txt', "w", encoding="utf-8")
# txt.writelines(lines)
# txt.close()

# v = open(r'C:\Users\Bratislav\Desktop\petnica projekat\data\values train 1000.txt', "w", encoding="utf-8")
# v.writelines(values)
# v.close()

# # while c < len(lines):
# #     line = lines[c]
# #     lines[c] = "#" + str(c) + " " + line 
# #     c+=1
# c = 0


# # while c < len(lines):
# #     line = lines[c]
# #     ind = line.find(" ")
# #     lines[c] = line[ind+1:]
# #     c+=1
# # print(lines[1][:10])

# # while c < len(lines):
# #     line = lines[c]
# #     if len(line) > 30:
# #         ind = line.find(" ")
# #         print("l",line[ind+10])
# #         if line[ind+12] == ";":
# #             lines[c] = line[:ind+12] + line[ind+13:]
# #             print(lines[c][0:30])
# #     c+=1

# while c < len(lines):
#     line = lines[c]
#     if len(line) < 10:
#         lines.remove(lines[c])        
#     else: 
#         c+=1
# # print(lines)
# # print(fixed)
# txt.close()





# dict = {"a": "b"}