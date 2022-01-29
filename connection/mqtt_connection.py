from paho.mqtt import client as mqtt_client

import random
import time
import json
import logging
from collections import defaultdict


broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'emqx'
password = 'public'
client = None

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

def load_client(entity):

    global client
    client = mqtt_client.Client(entity)
    print(client)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)

def start_client():
    global client
    client.loop_start()

def start_forever():
     global client
     client.loop_forever()

def publish():
    global client
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1

def subscribe():

    global client
    client.subscribe(topic)
    client.on_message = on_message