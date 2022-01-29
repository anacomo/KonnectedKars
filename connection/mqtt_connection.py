from paho.mqtt import client as mqtt_client

import random
import time
import json
import logging
from collections import defaultdict


broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"
# generate self.client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'emqx'
password = 'public'

class Client(object):
    def __init__(self):
        self.client = None
    def on_connect(self,client,userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    def on_message(self, userdata, msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    def load_client(self,entity):

        
        self.client = mqtt_client.Client(entity)
        print(self.client)
        self.client.username_pw_set(username, password)
        self.client.on_connect = self.on_connect
        self.client.connect(broker, port)

    def start_client(self):
        
        self.client.loop_start()

    def start_forever(self):
        
        self.client.loop_forever()

    def publish(self):
        
        msg_count = 0
        while True:
            time.sleep(1)
            msg = f"messages: {msg_count}"
            result = self.client.publish(topic, msg)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(f"Send `{msg}` to topic `{topic}`")
            else:
                print(f"Failed to send message to topic {topic}")
            msg_count += 1

    def subscribe(self):

        
        self.client.subscribe(topic)
        self.client.on_message = self.on_message