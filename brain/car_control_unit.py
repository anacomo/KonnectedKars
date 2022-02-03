'''
    This file implements the car control unit.
    
    Basically it stores the necessary car parameters and methods
    for our (virtual) IoT application to work.
'''

from tokenize import Double
import json
import phone_callls as caller


class CarControlUnit:
    
    def __init__(self):
        self.ambiental_lights_state = 'Off'
        self.emergency_phone_number = '0666666666'  #  TODO: replace with the actual number
        self.road_lights_state = 'Off'
        self.demisting_mechanism_state = 'Off'
        self.speed = None
        self.distance = None
        self.state_json = {}
        with open('../data/state.json', 'w') as json_file:
            json.dump(self.state_json, json_file)

    def set_ambiental_lights_state(self, state):
        self.ambiental_lights_state = state
        with open('../data/state.json', 'r') as json_file:
            data = json.load(json_file)
        data['ambiental_lights'] = self.ambiental_lights_state
        with open('../data/state.json', 'w') as json_file:
            json.dump(data, json_file)

    def set_road_lights_state(self, state):
        self.road_lights_state = state
        with open('../data/state.json', 'r') as json_file:
            data = json.load(json_file)
        data['road_lights'] = self.ambiental_lights_state
        with open('../data/state.json', 'w') as json_file:
            json.dump(data, json_file)

    def set_demisting_mechanism_state(self, state):
        self.demisting_mechanism_state = state
        with open('../data/state.json', 'r') as json_file:
            data = json.load(json_file)
        data['demisting_mechanism'] = self.demisting_mechanism_state
        with open('../data/state.json', 'w') as json_file:
            json.dump(data, json_file)

    def set_speed_value(self, speed):
        self.speed = speed
        with open('../data/state.json', 'r') as json_file:
            data = json.load(json_file)
        data['speed'] = self.speed
        with open('../data/state.json', 'w') as json_file:
            json.dump(data, json_file)

    def handle_message(self, message):
        #  How the message should look depending on the sensor that
        #  sent the information:
        #       => Weight sensor:
        #             [1] number
        #             e.g.  [1] 60
        #
        #       => Distance and speed sensor
        #             [2] number number
        #             e.g.  [2] 84 150
        #             84 = car speed (km/h); 150 = distance to the car in front (meters)
        #     
        #       => Crash sensor
        #             [3] number
        #             e.g. [3] 0
        #             0 = no crash happened; 1 = crash happened
        #
        #       => Lighting sensor
        #             [4] number
        #             e.g. [4] 0.80
        #             0 = completely dark; 1 = completely bright
        #
        #       => Demisting sensor
        #             [5] number
        #             e.g. [5] 1.55
        #             Glass should have a refraction index between 1.45 and 1.90
        #             Link: https://en.wikipedia.org/wiki/List_of_refractive_indices
        
        #  TODO: de verificat ca string-ul are formatul legit

        if message[1] == '1':
            weight = float(message[4:])
            if weight < 60:
                self.set_ambiental_lights_state('On')
                print('Am pornit luminile ambientale! Fitza\n')
            else:
                self.set_ambiental_lights_state('Off')
                print('Am stins luminile ambientale! Se aprind doar pentru domnisoare\n')
        elif message[1] == '2':
            data = message[4:].split()
            self.speed = float(data[0]) * 10 / 36 #transform speed in m/s not km/h
            self.distance = float(data[1])
            if self.distance/self.speed < 5:
                self.set_speed_value(0.001)
                print("Am pus frana (Alexandra nu mai pupa Masseratiuri)\n")
            else:
                self.set_speed_value(self.speed)
                print("O lasam pe Alexandra sa puna frana, vedem cum se descurca\n")
        elif message[1] == '3':
            crashStatus = True if message[-1] == '1' else False
            if crashStatus == True:
                #TODO call to emergency number
                caller.dial_numbers(caller.DIAL_NUMBERS);
                print("Masina a avut un accident\n")
            else:
                print("Masina este in stare buna\n")
        elif message[1] == '4':
            lighting_coef = float(message[4:])
            if lighting_coef < 0.4:
                self.set_road_lights_state('On')
                print('Am aprins farurile.\n')
            else:
                self.set_road_lights_state('Off')
                print('Am stins farurile.\n')
        elif message[1] == '5':
            refraction_index = float(message[4:])
            if refraction_index > 1.90:
                self.set_demisting_mechanism_state('On')
                print('Am pornit dezaburirea.\n')
            elif refraction_index >= 1.45:
                self.set_demisting_mechanism_state('Off')
                print('Am stins dezaburirea.\n')
            else:
                print('Impossible. What did the demisting sensor smoke?\n')
        elif message[1] == '6':
            print("\n-----------------------------------------\n")
            print("New request\n")
        else:
            print('Error :(')





