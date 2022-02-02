'''
    This file implements the HTTP REST API of our project.
    
    Presumably, various sensors would measure different car parameters
    and would then call this API on a regular basis (~every few seconds).
   
    The values retrieved from the sensors  are then passed to the control 
    unit of the car through MQTT.
   
    Afterwards, it is the job of the control unit to decide how to act based on
    the sensor values.
    
    Basically, the REST API wraps around the MQTT API.
'''

from re import S
from flask import Flask, request, jsonify
from threading import Thread
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap
import sensors.runner as sensors_runner
import time
import json
import eventlet
import logging
from paho.mqtt import client as mqtt_client

app = None
client = None
broker = 'broker.emqx.io'
port = 1883
topic = 'konnectedKars'
client_id = f'python-mqtt-0'
username = ''
password = ''

def get_mqtt_client():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish_message(client, message):
    result = client.publish(topic, message)
    status = result[0]

    if status == 0:
        print(f'Sent message `{message}`')
        return 'ok'
    else:
        print(f'Failed to send message to topic {topic}')
        return 'fail'

def create_app():
    global app
    app = Flask(__name__, instance_relative_config = True)
    client = get_mqtt_client()
    #client.loop_start()

    #  The saying goes that app never works without hello world.
    @app.route('/')
    def hello_world():

        message = '[6] '
        publish_message(client, message)
        return 'Hello World! New calls have been done!\n'
    
    #  We receive feedback from the weight sensor.
    #  Send the weight value as a message through MQTT.
    @app.route('/weight_sensor', methods = ['POST'])
    def weight_sensor_feedback():
        weight = request.json['weight']
        if not weight:
            return jsonify({'status': 'Weight value is required!'}), 403
        
        #  Create and publish the message
        message = '[1] ' + str(weight)
        return_value = publish_message(client, message)

        return jsonify({
            'status': return_value
        })

    #  We receive feedback from the distance and speed sensors.
    #  Send the speed and distance values through MQTT.
    @app.route('/speed_distance_sensor', methods = ['POST'])
    def speed_distance_sensor_feedback():
        speed = request.json['speed']
        distance = request.json['distance']

        if (not speed) or (not distance):
            return jsonify({'status': 'Speed and distance values are required!'}), 403

        #  Create and publish the message
        message = '[2] ' + str(speed) + ' ' + str(distance)
        return_value = publish_message(client, message)

        return jsonify({
            'status': return_value
        })

    #  We receive feedback from the distance and "crash sensor"
    #  Send the crash value (1 if the car is crashed, 0 otherwise) through MQTT.
    @app.route('/crash_sensor', methods = ['POST'])
    def crash_sensor_feedback():
        crash_status = request.json['crash_status']

        if not crash_status:
            return jsonify({'status': 'The crash status value is required!'}), 403

        #  Create and publish the message
        message = '[3] ' + str(crash_status)
        return_value = publish_message(client, message)

        return jsonify({
            'status': return_value
        })

    #  We receive feedback from the light sensor
    #  Send the luminosity value through MQTT
    @app.route('/light_sensor', methods = ['POST'])
    def light_sensor_feedback():
        luminosity = request.json['luminosity']

        if not luminosity:
            return jsonify({'status': 'The luminosity value is required!'}), 403

        #  Create and publish the message
        message = '[4] ' + str(luminosity)
        return_value = publish_message(client, message)

        return jsonify({
            'status': return_value
        })

    #  We receive feedback from the demisting sensor (aparent asta e 
    #  traducerea pt senzor de dezaburire)
    #  Send the refractive index through MQTT
    @app.route('/demisting_sensor', methods = ['POST'])
    def demisting_sensor_feedback():
        #  We pretend that the sensor measures the refractive index of the
        #  windscreen. Based on its value, the control unit will decide 
        #  whether to demist the windscreen or not.
        refraction_index = request.json['refraction_index']

        if not refraction_index:
            return jsonify({'status': 'The refraction index value is required!'}), 403

        #  Create and publish the message
        message = '[5] ' + str(refraction_index)
        return_value = publish_message(client, message)

        return jsonify({
            'status': return_value
        })
    
    return app

if __name__ == '__main__':
    create_app().run(threaded=True, port=8000)
