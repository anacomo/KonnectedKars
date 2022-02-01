from cgi import test
import random
from unittest import TextTestResult
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
def read_ambiental_lights():
    data_weight, test_weight = [], []
    fread = open(weight_passenger, 'r')
    ftest = open(weight_test, 'r')
    while True:
        l1 = fread.readline()
        l2 = fread.readline().split()
        if not l2: 
            break  # EOF
        data_weight.append(int(l2[1]))
    fread.close()

    for l1 in ftest:
        l1 = l1.split()
        test_weight.append(l1[1])
    ftest.close()

    return data_weight, test_weight


# * 2. AUTO BRAKE VALUES
def read_brake_values():
    data_brake, test_brake = [], []
    fread = open(auto_brake, 'r')
    ftest = open(brake_test, 'r')
    while True:
        line1 = fread.readline() # timestamp
        line2 = fread.readline().split() # speed
        line3 = fread.readline().split() # distance
        if not line3:
            break
        data_brake.append([int(line2[1]), int(line3[1])])
    for l1 in ftest:
        l1 = l1.split()
        test_brake.append(l1[1])
    fread.close(), ftest.close()
    
    return data_brake, test_brake

# * 3. CRASH STATUS
def read_crash_status():
    data_crash, test_crash = [], []
    fread = open(damage_situation, 'r')
    ftest = open(damage_test, 'r')
    
    for l1 in fread:
        l1 = l1.split()
        data_crash.append(int(l1[2]))
    for l1 in ftest:
        l1 = l1.split()
        test_crash.append(l1[2])
    fread.close(), ftest.close()

    return data_crash, test_crash

# * 4. LIGHT SENSOR
def read_light_sensor():
    data_light, test_light = [], []
    fread = open(lighting_values, 'r')
    ftest = open(lighting_test, 'r')
    while True:
        l1 = fread.readline()
        l2 = fread.readline().split()
        if not l2:
            break
        data_light.append(float(l2[-1]))
    for l1 in ftest:
        l1 = l1.split()
        test_light.append(l1[-1])
    fread.close(), ftest.close()
    return data_light, test_light

# * 5. DEMISTING SENSOR
def read_demising_sensor():
    data_dem, test_dem = [], []
    fread = open(refraction_values, 'r')
    ftest = open(refraction_test, 'r')
    while True:
        l1 = fread.readline()
        l2 = fread.readline().split()
        if not l2:
            break
        data_dem.append(float(l2[-1]))
    for l1 in ftest:
        test_dem.append(l1[-1])
    fread.close(), ftest.close()
    return data_dem, test_dem
