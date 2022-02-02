'''
    This file should make calls to the HTTP API (the one in app.py)
'''
from random import choice, weibullvariate
import requests
import random

from scipy import rand

def read_data():
    f_passenger = open("../data/weight_passenger.txt", "r")
    f_brake = open("../data/auto_brake.txt", "r")
    f_damage = open("../data/damage_situation.txt", "r")
    f_lighting = open("../data/lighting_values.txt", "r")
    f_refraction = open("../data/refraction_values.txt", "r")
    
    data_brake = []
    data_damage = []
    data_lighting = []
    data_refraction = []
    data_weight = []

    while True:
        timestampLine = f_passenger.readline()
        if timestampLine == '':
            break
        weightLine = f_passenger.readline()
        data_weight.append( (int)(weightLine[8:]) )

    while True:
        timestampLine = f_brake.readline()
        if timestampLine == '':
            break
        speedLine = f_brake.readline()
        distanceLine = f_brake.readline()
        data_brake.append( ( (int)(speedLine[6:]), (int)(distanceLine[9:]) ) )

    while True:
        parsedLine = f_damage.readline()
        if parsedLine == '':
            break
        data_damage.append(parsedLine)

    while True:
        timestampLine = f_lighting.readline()
        if timestampLine == '':
            break
        lightningLine = f_lighting.readline()
        data_lighting.append( (float)(lightningLine[10:]) )

    while True:
        timestampLine = f_refraction.readline()
        if timestampLine == '':
            break
        refractionLine = f_refraction.readline()
        data_refraction.append( (float)(refractionLine[12:16]) )   

    return data_brake, data_damage, data_lighting, data_refraction, data_weight

def makeWeightSensorRequest(data_weight, verbose=1):
    pload = {'weight' : random.choice(data_weight)}
    response = requests.post('http://127.0.0.1:8000/weight_sensor', json = pload)
    if verbose:
        print(response.text)
    return response.status_code

def makeSpeedDistanceRequest(data_brake, verbose=1):
    spd = random.choice(data_brake)
    pload = {'speed' : spd[0], 'distance' : spd[1]}
    response = requests.post('http://127.0.0.1:8000/speed_distance_sensor', json = pload)
    if verbose:
        print(response.text)
    return response.status_code

def makeCrashSensorRequest(data_damage, verbose=1):
    pload = {'crash_status' : random.choice(data_damage)}
    response = requests.post('http://127.0.0.1:8000/crash_sensor', json = pload)
    if verbose:
        print(response.text)
    return response.status_code

def makeLightSensorRequest(data_lighting, verbose=1):
    pload = {'luminosity' : random.choice(data_lighting)}
    response = requests.post('http://127.0.0.1:8000/light_sensor', json = pload)
    if verbose:
        print(response.text)
    return response.status_code

def makeDemistingSensorRequest(data_refraction, verbose=1):
    pload = {'refraction_index' : random.choice(data_refraction)}
    response = requests.post('http://127.0.0.1:8000/demisting_sensor', json = pload)
    if verbose:
        print(response.text)
    return response.status_code


def makeRequests(data_brake, data_damage, data_lighting, data_refraction, data_weight):

    makeWeightSensorRequest(data_weight)
    makeSpeedDistanceRequest(data_brake)
    makeCrashSensorRequest(data_damage)
    makeLightSensorRequest(data_lighting)
    makeDemistingSensorRequest(data_refraction)

if __name__ == '__main__':
    data_brake, data_damage, data_lighting, data_refraction, data_weight = read_data()
    makeRequests(data_brake, data_damage, data_lighting, data_refraction, data_weight)
