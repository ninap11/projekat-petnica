# from datetime import datetime
# from selenium import webdriver

# from selenium.webdriver import Chrome, ChromeOptions

# # options = ChromeOptions()
# # options.add_extension(r"D:\Downloads\bypass-paywalls-chrome-master\bypass-paywalls-chrome-master.crx")

# # driver = Chrome("C:/chromedriver_win32/chromedriver.exe", options=options)

# # # (optional) Look at the uploaded extension
# # driver.get("https://www.wsj.com/articles/former-uber-security-chief-charged-criminally-in-connection-with-2016-hack-11597953234?mod=searchresults&page=1&pos=1")

# a = "Aug. 12, 2020 6:01 am ET"
# a = a[:-6]
# a = a[:-4] + "0" + a[-4:]  

# print(a )
# date = datetime.strptime(a, "%b. %d, %Y %I:%M").date()
# print(date)

# txt = open(r'D:\Projekat\WSJmistake.txt', "r", encoding="utf-8")
# print(txt[0])

txt = open(r'D:\Projekat\data\test set.txt', "r", encoding="utf-8")
lines = txt.readlines()
txt.close()

txt2 = open(r'D:\Projekat\data\values test set.txt', "a", encoding="utf-8") 
values = []

c = 0
for line in lines:

    ind = line.index(" ")
    if len(line) > 20:
        if line[ind+12] == ";":
            idn = line[0:ind]
            print(idn)

            ind2 = line[ind+14:].find(";")
            ind2 += ind + 13
            title = line[ind+14:ind2]
            print(title)

            inp = str(input("v: "))
            full = idn + " " + inp + "\n"
            values.append(full)
            txt2.write(full)
            # print(values)
        else:
            # print("naha")
            idn = line[0:ind]
            print(idn)

            ind2 = line.find(";")
            title = line[ind+12:ind2]
            print(title)
            
            inp = str(input("v: "))
            full = idn + " " + inp + "\n"
            values.append(full)
            txt2.write(full)
            # print(values)

# txt2.writelines(values) 
txt2.close()   

# txt = open(r'D:\Projekat\New folder\train set.txt', "w", encoding="utf-8")
# txt.writelines(lines)


