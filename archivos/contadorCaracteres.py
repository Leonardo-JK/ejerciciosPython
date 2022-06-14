from os import strerror

file = input("Que archivo desea abrir? ")

try:
    fileOpen = open(file, "rt")

except IOError as err:
    print("Error al leer el archivo.", strerror(err.errno))

dic = {}

for line in fileOpen:
    for ch in line:
        if dic.get(ch.lower()) == None:
            dic[ch.lower()] = 1
        else:
            dic[ch.lower()] += 1

fileOpen.close()

#Order by recurrence:
for key in sorted(dic.keys(), key=dic.get): 
    print(key, "->", dic[key])
    
#Order by char:
for key in sorted(dic.keys(), key=dic.get): 
    print(key, "->", dic[key])