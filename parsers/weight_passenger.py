# modifica pathul absolut

f = open("weight_passenger.txt", "r")

data = []
while True:
    timestampLine = f.readline()
    if timestampLine == '':
        break

    weightLine = f.readline()

    data.append( (int)(weightLine[8:]) )

print(data)