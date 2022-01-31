'''
    This file should make calls to the HTTP API (the one in app.py)
'''
from random import weibullvariate
import requests

def makeWeightSensorRequest():
    pload = {'weight' : 50}
    weighSensorResponse = requests.post('http://127.0.0.1:8000/weight_sensor', data = pload)
    print(weighSensorResponse.text)

def makeSpeedDistanceRequest():
    pload = {'speed' : 50, 'distance' : 10}
    weighSensorResponse = requests.post('http://127.0.0.1:8000/speed_distance_sensor', data = pload)
    print(weighSensorResponse.text)

def makeCrashSensorRequest():
    pload = {'crash_status' : False}
    weighSensorResponse = requests.post('http://127.0.0.1:8000/crash_sensor', data = pload)
    print(weighSensorResponse.text)

def makeLightSensorRequest():
    pload = {'luminosity' : 50}
    weighSensorResponse = requests.post('http://127.0.0.1:8000/light_sensor', data = pload)
    print(weighSensorResponse.text)

def makeDemistingSensorRequest():
    pload = {'refraction_index' : 2}
    weighSensorResponse = requests.post('http://127.0.0.1:8000/demisting_sensor', data = pload)
    print(weighSensorResponse.text)


def makeRequests():

    makeWeightSensorRequest()
    makeSpeedDistanceRequest()
    makeCrashSensorRequest()
    makeLightSensorRequest()
    makeDemistingSensorRequest()

if __name__ == '__main__':
    makeRequests()
