# modifica pathul absolut

f = open("lighting_values.txt", "r")

data = []
while True:
    timestampLine = f.readline()
    if timestampLine == '':
        break

    lightningLine = f.readline()

    data.append( (float)(lightningLine[10:]) )
