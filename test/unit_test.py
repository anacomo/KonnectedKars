import unittest
import sys
sys.path.append("..")
from sensors.runner import *
from reader_prepare import *


class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.data_weight, self.test_weight = read_ambiental_lights()
        self.data_brake, self.test_brake = read_brake_values()
        self.data_crash, self.test_crash = read_crash_status()
        self.data_light, self.test_light = read_light_sensor()
        self.data_dem, self.test_dem = read_demising_sensor()
        
    # * 1. ambient lights
    def test_ambient_lights_status(self):
        status_code = makeWeightSensorRequest(self.data_weight, 0)
        self.assertEqual(status_code, 200)

    # * 2. auto brakes
    def test_speed_distance_status(self):
        status_code = makeSpeedDistanceRequest(self.data_brake, 0)
        self.assertEqual(status_code, 200)

    # * 3. crash status
    def test_crash_sensor(self):
        status_code = makeCrashSensorRequest(self.data_crash, 0)
        self.assertEqual(status_code, 200)

    # * 4. light sensor
    def test_light_sensor(self):
        status_code = makeLightSensorRequest(self.data_light, 0)
        self.assertEqual(status_code, 200)

    # * 5. demisting sensor
    def test_demisting_sensor(self):
        status_code = makeDemistingSensorRequest(self.data_dem, 0)
        self.assertEqual(status_code, 200)

# ----------- FAILURES ---------------------

    def test_failure_ambient_lights_status(self):
        pload = {'weight' : None}
        response = requests.post('http://127.0.0.1:8000/weight_sensor', json = pload)
        status_code = response.status_code
        self.assertEqual(status_code, 403)
   
    def test_failure_speed_distance_status(self):
        pload = {'speed' : None, 'distance' : None}
        response = requests.post('http://127.0.0.1:8000/speed_distance_sensor', json = pload)
        status_code = response.status_code
        self.assertEqual(status_code, 403)

    def test_failure_crash_sensor(self):
        pload = {'crash_status' : None}
        response = requests.post('http://127.0.0.1:8000/crash_sensor', json = pload)
        status_code = response.status_code
        self.assertEqual(status_code, 403)

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
    