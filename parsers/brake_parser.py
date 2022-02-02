# modifica pathul absolut

f = open("auto_brake.txt", "r")

data = []
while True:
    timestampLine = f.readline()
    if timestampLine == '':
        break

    speedLine = f.readline()
    distanceLine = f.readline()

    data.append( ( (int)(speedLine[6:]), (int)(distanceLine[9:]) ) )

#for i in range(len(data)):
#    print(data[i][0], data[i][1])