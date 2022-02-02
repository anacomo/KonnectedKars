import unittest
import sys
sys.path.append("..")
from reader_prepare import *
import json
import requests


class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.data_weight, self.test_weight = read_ambiental_lights()
        self.data_brake, self.test_brake = read_brake_values()
        self.data_crash, self.test_crash = read_crash_status()
        self.data_light, self.test_light = read_light_sensor()
        self.data_dem, self.test_dem = read_demising_sensor()
        
    # * 1. ambient lights
    def test_ambient_lights_status(self):
        pload = {'weight' : random.choice(self.data_weight)}
        response = requests.post('http://127.0.0.1:8000/weight_sensor', json = pload)
        self.assertEqual(response.status_code, 200)

    # * 2. auto brakes
    def test_speed_distance_status(self):
        spd = random.choice(self.data_brake)
        pload = {'speed' : spd[0], 'distance' : spd[1]}
        response = requests.post('http://127.0.0.1:8000/speed_distance_sensor', json = pload)
        self.assertEqual(response.status_code, 200)

    # * 3. crash status
    def test_crash_sensor(self):
        pload = {'crash_status' : random.choice(self.data_crash)}
        response = requests.post('http://127.0.0.1:8000/crash_sensor', json = pload)
        self.assertEqual(response.status_code, 200)

    # * 4. light sensor
    def test_light_sensor(self):
        pload = {'luminosity' : random.choice(self.data_light)}
        response = requests.post('http://127.0.0.1:8000/light_sensor', json = pload)
        self.assertEqual(response.status_code, 200)

    # * 5. demisting sensor
    def test_demisting_sensor(self):
        pload = {'refraction_index' : random.choice(self.data_dem)}
        response = requests.post('http://127.0.0.1:8000/demisting_sensor', json = pload)
        self.assertEqual(response.status_code, 200)

# ----------- FAILURES ---------------------
    # * 1. ambient lights
    def test_failure_ambient_lights_status(self):
        pload = {'weight' : None}
        response = requests.post('http://127.0.0.1:8000/weight_sensor', json = pload)
        status_code = response.status_code
        self.assertEqual(status_code, 403)
   
    # * 3. auto brakes
    def test_failure_speed_distance_status(self):
        pload = {'speed' : None, 'distance' : None}
        response = requests.post('http://127.0.0.1:8000/speed_distance_sensor', json = pload)
        status_code = response.status_code
        self.assertEqual(status_code, 403)

    # * 3. crash status
    def test_failure_crash_sensor(self):
        pload = {'crash_status' : None}
        response = requests.post('http://127.0.0.1:8000/crash_sensor', json = pload)
        status_code = response.status_code
        self.assertEqual(status_code, 403)

    # * 4. light sensor
    def test_failure_light_sensor(self):
        pload = {'luminosity' : None}
        response = requests.post('http://127.0.0.1:8000/light_sensor', json = pload)
        status_code = response.status_code
        self.assertEqual(status_code, 403)

    def test_failure_demisting_sensor(self):
        pload = {'refraction_index' : None}
        response = requests.post('http://127.0.0.1:8000/demisting_sensor', json = pload)
        status_code = response.status_code
        self.assertEqual(status_code, 403)
    
# ------------- VALUES ----------------------
    # * 1. ambient lights
    def test_func_ambiental(self):
        pload = {'weight' : random.choice(self.data_weight)}
        response = requests.post('http://127.0.0.1:8000/weight_sensor', json = pload)
        with open('../data/state.json', 'r') as json_file:
            data = json.load(json_file)
        self.assertIsNotNone(data['ambiental_lights'])

    # * 3. auto brakes
    def test_func_brakes(self):
        spd = random.choice(self.data_brake)
        pload = {'speed' : spd[0], 'distance' : spd[1]}
        response = requests.post('http://127.0.0.1:8000/speed_distance_sensor', json = pload)
        with open('../data/state.json', 'r') as json_file:
            data = json.load(json_file)
        self.assertIsNotNone(data['speed'])

    # * 4. light sensor
    def test_func_light(self):
        pload = {'luminosity' : random.choice(self.data_light)}
        response = requests.post('http://127.0.0.1:8000/light_sensor', json = pload)
        with open('../data/state.json', 'r') as json_file:
            data = json.load(json_file)
        self.assertIsNotNone(data['road_lights'])

    # * 5. demisting sensor
    def test_func_demisting(self):
        pload = {'refraction_index' : random.choice(self.data_light)}
        response = requests.post('http://127.0.0.1:8000/demisting_sensor', json = pload)
        with open('../data/state.json', 'r') as json_file:
            data = json.load(json_file)
        self.assertIsNotNone(data['demisting_mechanism'])
