
import random

txt_file = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\train set.txt", "r+", encoding= "utf-8-sig")
lines = txt_file.readlines()
# lines = []
txt_file.close()

values_file = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\values.txt", "r+", encoding= "utf-8-sig")
values = values_file.readlines()
values_file.close()

mistakes = []

os = []
ns = []
ps = []
os_v = []
ns_v = []
ps_v = []


i = 0
while i < len(lines):
    line = lines[i]
    id_number1 = line[:line.index(" ")].strip()
    
    value = values[i][line.index(" ") + 1 :].strip()
    id_number2 = values[i][:values[i].index(" ")]
    if id_number1 != id_number2:
        mistakes.append(line[:30])
    else:
        print(value)
        if value == "o":
            os.append(line)
            full = id_number1 + " " + value + "\n"
            os_v.append(full) 
        elif value == "n":
            ns.append(line)
            full = id_number1 + " " + value + "\n"
            ps_v.append(full) 
        else:
            ps.append(line)
            full = id_number1 + " " + value + "\n"
            ns_v.append(full) 
    i+=1
    
print(len(ns), len(ps), len(os))
length = min(len(ns), len(ps), len(os))

for i in range(375):
    print("len", length)
    r = random.randint(0, length-1)
    del os[r]
    del ns[r]
    del ps[r]
    del os_v[r]
    del ns_v[r]
    del ps_v[r]
    length -= 1
    
length = len(os)
for i in range(375):
    r = r = random.randint(0, length-1)
    del os[r]
    del os_v[r]
    length -=1    

lines = ns
values = ns_v

for i in os:
    lines.append(i)
for i in ps:
    lines.append(i)
for i in os_v:
    values.append(i)
for i in ps_v:
    values.append(i)

print(mistakes)

txt_file = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\trainset 150.txt", "w", encoding= "utf-8-sig")
txt_file.writelines(lines)
# lines = []
txt_file.close()

values_file = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\trainset values 150.txt", "w", encoding= "utf-8-sig")
values_file.writelines(values)
values_file.close()
