# * data folder
DATA = '../data/'

AUTO_BRAKE ='auto_brake'
DAMAGE_SIT = 'damage_situation'
LIGHT_VALS = 'lighting_values'
REFR_VALS = 'refraction_values'
WEIGHT_PASS = 'weight_passenger'

# * files to read
auto_brake = DATA + AUTO_BRAKE + '.txt'
damage_situation = DATA + DAMAGE_SIT + '.txt'
lighting_values = DATA + LIGHT_VALS + '.txt'
refraction_values = DATA + REFR_VALS + '.txt'
weight_passenger = DATA + WEIGHT_PASS + '.txt'

# * files to write
brake_test = DATA + AUTO_BRAKE + '_test' + '.txt'
damage_test = DATA + DAMAGE_SIT + '_test' + '.txt'
lighting_test = DATA + LIGHT_VALS + '_test' + '.txt'
refraction_test = DATA + REFR_VALS + '_test' + '.txt'
weight_test = DATA + WEIGHT_PASS + '_test' + '.txt'

# * 1. AMBIENTAL LIGHTS
filer = open(weight_passenger, 'r')
filew = open(weight_test, 'w')
while True:
    line1 = filer.readline()
    line2 = filer.readline().split()
    if not line2: 
        break  # EOF
    filew.write(line1[: -1])
    if int(line2[1]) < 60:
        filew.write(' On\n')
    else:
        filew.write(' Off\n')
filer.close()
filew.close()


# * 2. GENERATE AUTO BRAKE VALUES
filer = open(auto_brake, 'r')
filew = open(brake_test, 'w')
while True:
    line1 = filer.readline() # timestamp
    line2 = filer.readline().split() # speed
    line3 = filer.readline().split() # distance
    if not line3:
        break
    filew.write(line1[: -1])
    val = int(line3[1]) / int(line2[1])
    if val < 5:
        filew.write(' On\n')
    else:
        filew.write(' Off\n')
filer.close()
filew.close()

# * 3. CRASH STATUS
filer = open(damage_situation, 'r')
filew = open(damage_test, 'w')
while True:
    line1 = filer.readline().split()
    if not line1:
        break
    filew.write(line1[0] + ' ' + line1[1])
    if int(line1[-1]):
        filew.write(' On\n')
    else:
        filew.write(' Off\n')
filer.close()
filew.close()

# * 4. TURN ON LIGHT
filer = open(lighting_values, 'r')
filew = open(lighting_test, 'w')
while True:
    line1 = filer.readline()
    line2 = filer.readline().split()
    if not line2:
        break
    filew.write(line1[: -1])
    if float(line2[-1]) < 0.4:
        filew.write(' On\n')
    else:
        filew.write(' Off\n')
filer.close()
filew.close()

# * 5. DEMISTING SENSOR
filer = open(refraction_values, 'r')
filew = open(refraction_test, 'w')
while True:
    line1 = filer.readline()
    line2 = filer.readline().split()
    if not line2:
        break
    filew.write(line1[: -1])
    if float(line2[-1]) > 1.9:
        filew.write(' On\n')
    else:
        filew.write(' Off\n')
filer.close()
filew.close()