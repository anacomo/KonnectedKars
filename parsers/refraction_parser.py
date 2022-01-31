# modifica pathul absolut

f = open("refraction_values.txt", "r")

data = []
while True:
    timestampLine = f.readline()
    if timestampLine == '':
        break

    refractionLine = f.readline()

    data.append( (float)(refractionLine[12:16]) )
