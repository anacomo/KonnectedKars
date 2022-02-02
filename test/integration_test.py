import unittest
import sys
sys.path.append("..")
import requests
from reader_prepare import *

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.data_weight, self.test_weight = read_ambiental_lights()
        self.data_brake, self.test_brake = read_brake_values()
        self.data_crash, self.test_crash = read_crash_status()
        self.data_light, self.test_light = read_light_sensor()
        self.data_dem, self.test_dem = read_demising_sensor()
    
    def test_app(self):
        pload = {'weight' : random.choice(self.data_weight)}
        response = requests.post('http://127.0.0.1:8000/weight_sensor', json = pload)
        self.assertEqual(response.status_code, 200)

        spd = random.choice(self.data_brake)
        pload = {'speed' : spd[0], 'distance' : spd[1]}
        response = requests.post('http://127.0.0.1:8000/speed_distance_sensor', json = pload)
        self.assertEqual(response.status_code, 200)

        pload = {'crash_status' : random.choice(self.data_crash)}
        response = requests.post('http://127.0.0.1:8000/crash_sensor', json = pload)
        self.assertEqual(response.status_code, 200)

        pload = {'luminosity' : random.choice(self.data_light)}
        response = requests.post('http://127.0.0.1:8000/light_sensor', json = pload)
        self.assertEqual(response.status_code, 200)

        pload = {'refraction_index' : random.choice(self.data_dem)}
        response = requests.post('http://127.0.0.1:8000/demisting_sensor', json = pload)
        self.assertEqual(response.status_code, 200)

        pload = {'weight' : None}
        response = requests.post('http://127.0.0.1:8000/weight_sensor', json = pload)
        status_code = response.status_code
        self.assertEqual(status_code, 403)

        pload = {'speed' : None, 'distance' : None}
        response = requests.post('http://127.0.0.1:8000/speed_distance_sensor', json = pload)
        status_code = response.status_code
        self.assertEqual(status_code, 403)

        pload = {'crash_status' : None}
        response = requests.post('http://127.0.0.1:8000/crash_sensor', json = pload)
        status_code = response.status_code
        self.assertEqual(status_code, 403)

        pload = {'luminosity' : None}
        response = requests.post('http://127.0.0.1:8000/light_sensor', json = pload)
        status_code = response.status_code
        self.assertEqual(status_code, 403)

        pload = {'refraction_index' : None}
        response = requests.post('http://127.0.0.1:8000/demisting_sensor', json = pload)
        status_code = response.status_code
        self.assertEqual(status_code, 403)
