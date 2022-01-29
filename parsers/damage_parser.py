# da pathul absolut pt damage care e in data sau unde va fi daca-l mutam

f = open("damage_situation.txt", "r")

data = []
while True:
    parsedLine = f.readline()
    if parsedLine == '':
        break
    data.append(parsedLine)


#for i in range(len(data)):
#    print(data[i])