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
    
    def test_ambiental_val(self):
        pass

    def test_speed(self):
        pass

    def test_crash(self):
        pass

    def test_light(self):
        pass

    def test_refraction(self):
        pass