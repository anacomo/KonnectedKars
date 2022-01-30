'''
    This file implements the car control unit.
    
    Basically it stores the necessary car parameters and methods
    for our (virtual) IoT application to work.
'''

class CarControlUnit:
    
    def __init__(self):
        self.ambiental_lights_state = 'Off'
        self.emergency_phone_number = '0666666666'  #  TODO: replace with the actual number
        self.road_lights_state = 'Off'
        self.demisting_mechanism_state = 'Off'

    def set_ambiental_lights_state(self, state):
        self.ambiental_lights_state = state

    def set_road_lights_state(self, state):
        self.road_lights_state = state

    def set_demisting_mechanism_state(self, state):
        self.demisting_mechanism_state = state

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
            weight = int(message[4:])
            if weight < 60:
                self.set_ambiental_lights_state('On')
                print('Am pornit luminile ambientale! Fitza')
            else:
                self.set_ambiental_lights_state('Off')
                print('Am stins luminile ambientale! Se aprind doar pentru domnisoare')
        elif message[1] == '2':
            #  TODO: implement this
            pass
        elif message[1] == '3':
            #  TODO: implement this
            pass
        elif message[1] == '4':
            lighting_coef = int(message[4:])
            if lighting_coef < 0.4:
                self.set_road_lights_state('On')
                print('Am aprins farurile.')
            else:
                self.set_road_lights_state('Off')
                print('Am stins farurile.')
        elif message[1] == '5':
            refraction_index = int(message[4:])
            if refraction_index > 1.90:
                self.set_demisting_mechanism_state('On')
                print('Am pornit dezaburirea.')
            elif refraction_index >= 1.45:
                self.set_demisting_mechanism_state('Off')
                print('Am stins dezaburirea.')
            else:
                print('Impossible. What did the demisting sensor smoke?')
        else:
            print('Error :(')





